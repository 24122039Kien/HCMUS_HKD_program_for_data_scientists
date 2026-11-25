# NHẬT KÝ LÀM VIỆC – Đăng (TV2)
- **Đồ án:** CSC17104 – Lập trình cho Khoa học Dữ liệu
- **Đề tài:** Phân tích và Dự báo Tỷ lệ Tự tử Toàn cầu (Suicide Rates 1985–2016)
- **Thành viên:** Đăng – Thành viên 2 (TV2)
- **Ngày bắt đầu:** 09/11/2026

---

## GIAI ĐOẠN 1: THU THẬP & KHÁM PHÁ DỮ LIỆU (EDA) — 03/11 – 09/11

### Ngày 09/11/2026

#### Công việc đã hoàn thành

Tạo file notebook EDA chuyên sâu cho nhóm cột số & kinh tế theo phân công TV2:

**File tạo ra:** `notebooks/tv2_eda_numerical.ipynb`

---

#### Chi tiết nội dung notebook

**Cell 0 – Setup môi trường**
- Import các thư viện: `numpy`, `pandas`, `matplotlib`, `seaborn`, `scipy`
- Import module dùng chung từ `src/`: `set_academic_style()`, `save_figure()`, `check_row_count()`
- Đọc file `data/raw/master.csv` vào DataFrame

**Cell 1 – Xử lý lỗi tên cột & ép kiểu**
- Phát hiện và xử lý lỗi khoảng trắng thừa trong tên cột GDP gốc: `' gdp_for_year ($) '` → `'gdp_for_year'`
- Đổi tên chuẩn hóa: `'suicides/100k pop'` → `'suicides_per_100k'`, `'gdp_per_capita ($)'` → `'gdp_per_capita'`
- Ép kiểu `gdp_for_year`: loại bỏ dấu phẩy hàng nghìn rồi chuyển `str` → `int64`

**Cell 2 – Thống kê mô tả tổng quan 5 cột số**
- Bảng thống kê: count, mean, std, min, 25%, 50%, 75%, max
- Bổ sung: missing (%), skewness, kurtosis cho cả 5 cột

**Cell 3.1 – Sanity checks**
- Kiểm tra `suicides_no < 0` (ca tự tử âm)
- Kiểm tra `population == 0` (mẫu số bằng 0, gây lỗi phép chia)
- Kiểm tra mâu thuẫn logic: `suicides_no = 0` nhưng `suicides_per_100k > 0`
- Kiểm tra `gdp_per_capita <= 0`

**Cell 3.2 – Kiểm tra sai số làm tròn**
- Tính lại tỷ lệ theo công thức chuẩn: $100{,}000 \times \frac{\text{suicides\_no}}{\text{population}}$
- So sánh với cột `suicides_per_100k` gốc → báo cáo sai số tuyệt đối tối đa và trung bình

**Cell 3.3 – Kiểm tra tính nhất quán GDP trong country-year**
- Với mỗi cặp `(country, year)`, đếm số giá trị GDP khác nhau giữa các dòng con
- Xác nhận GDP nhất quán → an toàn khi gộp bằng `FIRST`

**Cell 4 – Biểu đồ 1: Phân phối 5 cột số**
- Vẽ 2 hàng × 5 cột: Histogram + KDE (hàng trên) và Boxplot (hàng dưới)
- Annotate skewness trên mỗi histogram
- Lưu ra: `data/processed/tv2_fig1_distribution.png`

**Cell 5 – Biểu đồ 2: Phân tích outlier dân số**
- Gộp dữ liệu về cấp `(country, year)`: tính tổng ca, tổng dân số, tỷ lệ / 100k
- Tính IQR fence, xác định quốc gia dân số siêu nhỏ và siêu lớn
- Scatter plot: dân số (thang log) vs tỷ lệ / 100k, highlight quốc gia dân số < 100k
- Annotate top 5 điểm outlier cực đoan (Grenada, San Marino, ...)
- Lưu ra: `data/processed/tv2_fig2_outlier_population.png`

**Cell 6 – Biểu đồ 3: Ma trận tương quan**
- Tính tương quan Pearson và Spearman ở cấp `country-year`
- Heatmap song song (Pearson | Spearman)
- Nhận xét: tương quan GDP ↔ Tỷ lệ bị nhiễu bởi đặc thù quốc gia → Q3 sẽ dùng First-difference
- Lưu ra: `data/processed/tv2_fig3_correlation.png`

**Cell 7 – 7 Quy tắc làm sạch đề xuất cho Giai đoạn 2**

| Mã | Tên quy tắc | Nội dung |
|----|-------------|----------|
| R1 | Chuẩn hóa tên cột | Strip khoảng trắng + đổi tên cột GDP ✅ ĐÃ THỰC HIỆN |
| R2 | Ép kiểu gdp_for_year | str → int64 ✅ ĐÃ THỰC HIỆN |
| R3 | Lọc dân số = 0 | Loại bỏ dòng population == 0 trước khi tính tỷ lệ |
| R4 | Dùng rate_recalculated | Tính lại tỷ lệ từ suicides_no / population thay cột gốc |
| R5 | Quy tắc gộp country-year | SUM(ca), SUM(dân), FIRST(GDP); tỷ lệ = 100k × SUM/SUM |
| R6 | Xử lý outlier siêu nhỏ | Xem xét lọc quốc gia dân số TB < 100,000 cho Q3/Q4 |
| R7 | Biến trễ GDP | Tạo gdp_per_capita_lag1 theo quốc gia, báo cáo số dòng mất do NaN |

**Cell 8 – Bảng kiểm tra chất lượng biến số (TV2 Deliverable)**
- Tổng hợp 5 cột: kiểu gốc, kiểu sau chuẩn hóa, thiếu (%), skewness, kết quả sanity check, hành động đề xuất

**Cell 9 – Tóm tắt EDA**
- **5 Key Observations** từ nhóm cột số/kinh tế
- **Serious Data Quality Issues** đã phát hiện
- **Preprocessing Plan** cho Giai đoạn 2

---

#### Push lên GitHub

- Tạo nhánh: `feature/eda-dang`
- Add file: `notebooks/tv2_eda_numerical.ipynb`
- Commit message: `feat(tv2): EDA chuyen sau nhom cot so & kinh te (Giai doan 1)`
- Push: `git push -u origin feature/eda-dang`

---

## Kế hoạch giai đoạn 2 và trạng thái sau khi chạy ngày 23/11/2026

- [x] Đặt file `data/raw/master.csv` vào thư mục (tải từ Kaggle) rồi chạy lại notebook để xem kết quả thực tế
- [x] Viết `src/visualization.py` bổ sung (nếu TV1 chưa tạo đủ hàm cần dùng)
- [x] Tạo notebook `notebooks/02_analysis_q3_q4.ipynb` cho Q3 và Q4
- [x] Viết đặc tả chi tiết Mục 3.3 cho Q3 và Q4 (Target user, Motivation, Quyết định hỗ trợ)
- [x] Tiền xử lý Q3: gộp `(country, year)`, tạo lag 1 năm, tính `%ΔGDP` và `ΔRate`, in số dòng trước/sau
- [x] Tiền xử lý Q4: tách 2 giai đoạn 1995–2000 vs 2010–2015, chuẩn bị ASR với dân số chuẩn WHO
- [x] Dựng biểu đồ sơ bộ cho Q3 và Q4

## Ngày 23/11/2026 · Hoàn thiện Q3–Q4 và kiểm tra bài nhóm

| Phần việc | Việc đã thực hiện và kết quả |
| --- | --- |
| Giai đoạn 1 · EDA | Chạy lại notebook 01 trên 27.820 dòng dữ liệu Kaggle. Sửa cách tra kiểu dữ liệu GDP khi tên cột gốc có khoảng trắng. Phần EDA từ nhánh `feature/eda-dang` hiện nằm trong notebook 01 của nhóm. |
| Giai đoạn 2 · GDP và cơ cấu tuổi | Gộp ca và dân số theo quốc gia–năm. Q3 ghép đúng năm lịch, thu được 2.148 cặp một năm của 96 nước và 2.028 cặp hai năm. Q4 giữ cùng 49 nước có đủ tuổi và giới trong cả hai giai đoạn 1995–2000 và 2010–2015. |
| Giai đoạn 3 · Phân tích và tổng kết | Hoàn thành bốn biểu đồ Q3–Q4. Kiểm tra Q3 theo độ trễ, ngưỡng biến động GDP và nhóm thu nhập. Với Q4, đối chiếu chuẩn WHO và chuẩn mẫu trên 98 kết quả quốc gia–giai đoạn. Thay đổi cơ cấu tuổi đóng góp +0,81 ca/100.000 và thay đổi tỷ lệ riêng theo tuổi đóng góp −2,90, cho mức thay đổi thô −2,09. |
| Giai đoạn 4 · Slide và tái lập | Biên tập slide 9 trang cho bài nói 15 phút, mỗi thành viên 5 phút. Rà soát Q5–Q6 của TV3. Chạy 3 notebook nhóm và notebook Q3–Q4 độc lập trong môi trường Conda mới, hoàn thành 66/66 ô code. Q6 tái lập MAE 2,065 so với 2,213 của mô hình giữ nguyên tỷ lệ năm trước. |

**Bàn giao trên nhánh `feature/q3-q4`.** [Notebook Q3–Q4](notebooks/02_analysis_q3_q4.ipynb) chứa các bảng kết quả và bốn hình. [Mục 3.5 của bài nhóm](notebooks/02_analysis.ipynb) tổng hợp sáu câu hỏi, giới hạn và hướng mở rộng. [Slide](slides.pdf) và [biên bản tái lập](Docs/TV2_sprints.md) đi kèm số liệu, phiên bản thư viện và ghi chú khi chạy trên Windows.

**Trước khi nộp.** Đăng tự duyệt bản nháp phản tư đã khai báo trong [nhật ký AI](LLM_USAGE.md). Các số liệu Q1–Q2 dùng cho slide do TV2 tính đối chiếu, cần so lại khi TV1 ghép kết quả chính thức.
