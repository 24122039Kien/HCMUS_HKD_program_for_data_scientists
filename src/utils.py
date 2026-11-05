"""
utils.py - Module chứa các hàm xử lý dữ liệu, tính toán thống kê dùng chung
"""

import numpy as np
import pandas as pd


def check_row_count(df_before: pd.DataFrame, df_after: pd.DataFrame, step_description: str = ""):
    """
    Quy tắc bắt buộc của đề bài (Mục 3.4):
    In và báo cáo số dòng trước/sau mỗi bước biến đổi dữ liệu (lọc, ghép, xóa).
    """
    n_before = len(df_before)
    n_after = len(df_after)
    diff = n_after - n_before
    pct = (diff / n_before) * 100 if n_before > 0 else 0
    print(f"[{step_description}]")
    print(f"  • Số dòng trước : {n_before:,}")
    print(f"  • Số dòng sau   : {n_after:,}")
    print(f"  • Thay đổi      : {diff:+,} dòng ({pct:+.2f}%)\n")


def calculate_aggregated_rate(df: pd.DataFrame, suicides_col: str = "suicides_no", pop_col: str = "population") -> float:
    """
    Tính tỷ lệ tự tử tổng hợp chuẩn xác: 100,000 * (Tổng số ca / Tổng dân số)
    Tránh bẫy Simpson's Paradox khi lấy trung bình cộng cột tỷ lệ.
    """
    total_suicides = df[suicides_col].sum()
    total_pop = df[pop_col].sum()
    if total_pop == 0:
        return 0.0
    return float(100_000 * (total_suicides / total_pop))


def calculate_asr(df: pd.DataFrame, standard_population: dict, age_col: str = "age", 
                  suicides_col: str = "suicides_no", pop_col: str = "population") -> float:
    """
    Tính Tỷ lệ Chuẩn hóa Trực tiếp theo Độ tuổi (Direct Age-Standardized Rate - ASR).
    ASR = Sum(Rate_i * w_i) / Sum(w_i) với w_i là trọng số dân số chuẩn.
    """
    grouped = df.groupby(age_col).agg({suicides_col: "sum", pop_col: "sum"}).reset_index()
    grouped["rate"] = 100_000 * (grouped[suicides_col] / grouped[pop_col])
    
    numerator = 0.0
    denominator = 0.0
    for _, row in grouped.iterrows():
        age_group = row[age_col]
        weight = standard_population.get(age_group, 0)
        numerator += row["rate"] * weight
        denominator += weight
        
    return float(numerator / denominator) if denominator > 0 else 0.0


def cluster_bootstrap_ci(df: pd.DataFrame, cluster_col: str, calc_func, 
                         n_bootstraps: int = 1000, ci: float = 95.0, random_state: int = 42) -> tuple:
    """
    Non-parametric Cluster Bootstrap để tính Khoảng tin cậy (Confidence Interval).
    Lấy mẫu lại theo cấp cụm (Cluster - ví dụ theo quốc gia) để giữ nguyên cấu trúc phụ thuộc.
    """
    rng = np.random.RandomState(random_state)
    unique_clusters = df[cluster_col].unique()
    boot_estimates = []
    
    for _ in range(n_bootstraps):
        sampled_clusters = rng.choice(unique_clusters, size=len(unique_clusters), replace=True)
        # Ghép các dòng thuộc các cụm được lấy mẫu
        boot_df = pd.concat([df[df[cluster_col] == c] for c in sampled_clusters], ignore_index=True)
        boot_estimates.append(calc_func(boot_df))
        
    alpha = (100.0 - ci) / 2.0
    lower_bound = float(np.percentile(boot_estimates, alpha))
    upper_bound = float(np.percentile(boot_estimates, 100.0 - alpha))
    return lower_bound, upper_bound
