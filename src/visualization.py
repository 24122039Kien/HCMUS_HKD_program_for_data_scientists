"""
visualization.py - Module chuẩn hóa style đồ thị học thuật và hàm lưu ảnh
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def set_academic_style():
    """
    Thiết lập style chuẩn học thuật đồng bộ cho toàn bộ đồ thị trong đồ án:
    Font rõ ràng, nền trắng lưới mờ, kích thước chữ hài hòa, bảng màu colorblind-friendly.
    """
    sns.set_theme(style="whitegrid", font="DejaVu Sans")
    plt.rcParams.update({
        "font.size": 11,
        "axes.labelsize": 12,
        "axes.titlesize": 13,
        "axes.titleweight": "bold",
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "legend.fontsize": 10,
        "figure.titlesize": 14,
        "figure.dpi": 100,
        "axes.edgecolor": "#cccccc",
        "grid.color": "#e0e0e0",
        "grid.linestyle": "--",
        "grid.alpha": 0.7,
    })


def save_figure(fig, filename: str, dpi: int = 300):
    """
    Lưu biểu đồ chất lượng cao phục vụ chèn vào slides.pdf hoặc báo cáo
    """
    fig.savefig(filename, dpi=dpi, bbox_inches="tight")
    print(f"-> Đã lưu biểu đồ: {filename}")


def plot_gdp_changes(pairs):
    fig, axes = plt.subplots(1, 3, figsize=(13, 4.4), sharex=True, sharey=True)
    for ax, band, color in zip(axes, ["Thấp", "Trung bình", "Cao"], sns.color_palette("colorblind", 3)):
        part = pairs.loc[pairs.income.eq(band)]
        sns.regplot(data=part, x="gdp_change", y="rate_change", ci=None, ax=ax, color=color,
                    scatter_kws={"alpha": .35, "s": 13}, line_kws={"lw": 2})
        ax.axhline(0, color="grey", lw=.7)
        ax.set(title=f"GDP {band.lower()} · n = {len(part)}", xlabel="Thay đổi GDP/người (%)")
        ax.set_ylabel("")
    axes[0].set_ylabel("Thay đổi tỷ lệ (ca/100.000)")
    fig.suptitle("Sai phân một năm trong cùng quốc gia")
    fig.tight_layout()
    return fig


def plot_crisis(panel):
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
    for ax, country in zip(axes, ["Japan", "United States"]):
        rows = panel.loc[panel.country.eq(country) & panel.year.between(2003, 2013)].set_index("year")
        rows = rows.reindex(range(2003, 2014))
        right = ax.twinx()
        a, = ax.plot(rows.index, rows.gdp, "o-", color="#145c79", label="GDP/người")
        b, = right.plot(rows.index, rows.rate, "s--", color="#a75128", label="Tỷ lệ")
        ax.axvspan(2008, 2009, color="grey", alpha=.15)
        ax.set(title=f"{country} · n = {rows.rate.count()} năm", xlabel="Năm",
               ylabel="GDP/người (USD hiện hành)")
        right.set_ylabel("Ca/100.000 dân từ 5 tuổi")
        right.grid(False)
        ax.legend(handles=[a, b], fontsize=9, loc="upper left")
    fig.suptitle("GDP và tỷ lệ ghi nhận quanh giai đoạn 2008–2009")
    fig.tight_layout()
    return fig


def plot_crude_asr(delta):
    top = delta.nlargest(15, "Δ dân số 55+ (điểm %)").iloc[::-1]
    fig, ax = plt.subplots(figsize=(9, 6.8))
    y = np.arange(len(top))
    ax.hlines(y, top["Δ WHO"], top["Δ Thô"], color="#93a7af")
    ax.scatter(top["Δ Thô"], y, label="Thô", color="#ad542c")
    ax.scatter(top["Δ WHO"], y, label="Chuẩn WHO", color="#145c79", marker="D")
    ax.axvline(0, color="grey", lw=1)
    ax.set(yticks=y, yticklabels=top.index, ylabel="Quốc gia",
           xlabel="Thay đổi từ 1995–2000 đến 2010–2015 (ca/100.000 dân từ 5 tuổi)",
           title=f"{len(top)} nước tăng tỷ trọng dân số 55+ nhanh nhất (n = {len(delta)} nước)")
    ax.legend()
    fig.tight_layout()
    return fig


def plot_age_shares(shares, countries):
    fig, ax = plt.subplots(figsize=(9, 3.7))
    data = shares.mul(100).rename(columns=lambda label: label.replace(" years", ""))
    data.plot.barh(stacked=True, color=sns.color_palette("viridis", data.shape[1]), ax=ax)
    ax.set(xlabel="Tỷ trọng dân số từ 5 tuổi (%)", ylabel="Giai đoạn", xlim=(0, 100),
           title=f"Cơ cấu tuổi của cùng {countries} nước")
    ax.legend(title="Tuổi", ncol=6, loc="upper center", bbox_to_anchor=(.5, -.25))
    fig.tight_layout()
    return fig

