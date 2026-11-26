"""Country-year GDP differences and direct age standardization for Q3–Q4."""
import numpy as np
import pandas as pd

from .utils import check_row_count


# WHO 2000–2025, Table 4 (Ahmad et al., 2001). Group the original 5-year
# bands and condition on ages 5+, the population observed in master.csv.
WHO = pd.Series({
    "5-14 years": 8.69 + 8.60,
    "15-24 years": 8.47 + 8.22,
    "25-34 years": 7.93 + 7.61,
    "35-54 years": 7.15 + 6.59 + 6.04 + 5.37,
    "55-74 years": 4.55 + 3.72 + 2.96 + 2.21,
    "75+ years": 1.52 + 0.91 + 0.44 + 0.15 + 0.04 + 0.005,
})
PERIODS = ["1995–2000", "2010–2015"]
KEY = ["country", "year"]


def complete_years(raw):
    data = raw.rename(columns=lambda name: name.strip()).rename(
        columns={"gdp_per_capita ($)": "gdp", "gdp_for_year ($)": "gdp_total"}
    )
    if data.duplicated(KEY + ["age", "sex"]).any():
        raise ValueError("Khóa quốc gia–năm–tuổi–giới bị trùng.")
    valid = (data.age.isin(WHO.index) & data.sex.isin(["male", "female"])
             & data.population.gt(0) & data.suicides_no.ge(0))
    rows = data.loc[valid].copy()
    check_row_count(data, rows, "Nhãn hợp lệ, dân số dương và số ca không âm")
    size = rows.groupby(KEY).age.transform("size")
    full = rows.loc[size.eq(12)].copy()
    check_row_count(rows, full, "Đủ 6 nhóm tuổi × 2 giới tại mỗi quốc gia–năm")
    return full


def country_years(full):
    grouped = full.groupby(KEY)
    if not grouped.gdp.nunique(dropna=False).eq(1).all():
        raise ValueError("GDP không đồng nhất trong một quốc gia–năm.")
    panel = grouped.agg(cases=("suicides_no", "sum"), pop=("population", "sum"),
                        gdp=("gdp", "first")).reset_index()
    check_row_count(full, panel, "Gộp thành quốc gia–năm, cộng số ca và dân số")
    panel = panel.assign(rate=100_000 * panel.cases / panel["pop"])
    usable = panel.loc[panel.gdp.gt(0)].copy()
    check_row_count(panel, usable, "GDP bình quân dương để tính phần trăm")
    # Each country counts once when estimating the income terciles.
    typical_gdp = usable.groupby("country").gdp.median()
    # Nearest-rank terciles avoid floating-point interpolation at a boundary.
    ordered = typical_gdp.sort_values()
    lower, upper = ordered.iloc[[(len(ordered) - 1) // 3, (2 * len(ordered) - 1) // 3]]
    bands = pd.Series(np.select([typical_gdp.le(lower), typical_gdp.le(upper)],
                                ["Thấp", "Trung bình"], default="Cao"), index=typical_gdp.index)
    return usable.assign(income=usable.country.map(bands))


def changes(panel, lag):
    previous = panel[KEY + ["rate", "gdp"]].copy()
    previous["year"] += lag
    pairs = panel.merge(previous, on=KEY, suffixes=("", "_prior"), validate="one_to_one")
    check_row_count(panel, pairs, f"Có cùng nước ở đúng năm t−{lag}")
    return pairs.assign(gdp_change=100 * (pairs.gdp / pairs.gdp_prior - 1),
                        rate_change=pairs.rate - pairs.rate_prior)


def associations(one, two):
    samples = {"1 năm": one, "2 năm": two,
               "1 năm, |ΔGDP| ≤ 20%": one.loc[one.gdp_change.abs().le(20)]}
    for label in ["Thấp", "Trung bình", "Cao"]:
        samples[f"1 năm, GDP {label.lower()}"] = one.loc[one.income.eq(label)]
    records = []
    for label, sample in samples.items():
        x, y = sample.gdp_change, sample.rate_change
        records.append([label, len(sample), sample.country.nunique(), x.corr(y),
                        x.corr(y, method="spearman"), 10 * x.cov(y) / x.var()])
    return pd.DataFrame(records, columns=["Mẫu", "Số cặp", "Số nước", "Pearson r",
                                         "Spearman ρ", "Δ tỷ lệ / +10% GDP"]).set_index("Mẫu")


def period_cohort(full):
    early = full.year.between(1995, 2000)
    late = full.year.between(2010, 2015)
    selected = full.loc[early | late].copy()
    selected["period"] = np.where(selected.year.le(2000), *PERIODS)
    check_row_count(full, selected, "Hai cửa sổ, mỗi cửa sổ 6 năm lịch")
    years = selected.groupby("country").year.transform("nunique")
    cohort = selected.loc[years.eq(12)].copy()
    check_row_count(selected, cohort, "Cùng quốc gia đủ cả 12 năm")
    return cohort


def age_comparison(cohort, empirical, by_country=True):
    """Return period rates, their decomposition, and the observed age shares."""
    if not by_country:
        cohort = cohort.assign(country="Tất cả nước trong mẫu")
    keys = ["country", "period"]
    totals = cohort.groupby(keys + ["age"])[["suicides_no", "population"]].sum()
    check_row_count(cohort, totals, "Cộng số ca và dân số theo giai đoạn và nhóm tuổi")
    pop = totals.population.unstack("age")[WHO.index]
    rates = 100_000 * totals.suicides_no.unstack("age")[WHO.index] / pop
    share = pop.div(pop.sum(axis=1), axis=0)
    weights = pd.concat([WHO.rename("WHO"), empirical.rename("Mẫu")], axis=1).loc[WHO.index]
    if rates.isna().any().any() or not weights.gt(0).all().all():
        raise ValueError("Thiếu nhóm tuổi hoặc trọng số tham chiếu.")
    result = rates.dot(weights / weights.sum())
    result["Thô"] = (share * rates).sum(axis=1)
    # Symmetric Kitagawa decomposition. Components add to the crude change.
    r0, r1 = (rates.xs(p, level="period") for p in PERIODS)
    s0, s1 = (share.xs(p, level="period") for p in PERIODS)
    composition = ((s1 - s0) * (r1 + r0) / 2).sum(axis=1)
    risk = ((r1 - r0) * (s1 + s0) / 2).sum(axis=1)
    old, new = (result.xs(p, level="period") for p in PERIODS)
    delta = (new - old).add_prefix("Δ ")
    delta["Cơ cấu tuổi"] = composition
    delta["Tỷ lệ theo tuổi"] = risk
    delta["Cơ cấu / Δ thô (%)"] = 100 * composition / delta["Δ Thô"].where(delta["Δ Thô"].abs() > 1e-8)
    delta["Δ dân số 55+ (điểm %)"] = 100 * (s1 - s0).iloc[:, -2:].sum(axis=1)
    np.testing.assert_allclose(composition + risk, delta["Δ Thô"], atol=1e-9)
    if not by_country:
        return result.droplevel("country"), delta, share.droplevel("country")
    return result, delta, share
