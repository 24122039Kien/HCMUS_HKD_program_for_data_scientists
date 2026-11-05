"""
visualization.py - Module chuẩn hóa style đồ thị học thuật và hàm lưu ảnh
"""

import matplotlib.pyplot as plt
import seaborn as sns


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
