# Báo cáo tiến độ 03: rà soát phần TV3 trước khi khóa bài

**Người làm:** Nguyễn Đỗ Bảo Kiên (TV3), MSSV 24122039
**Ngày:** 25/11/2026
**Nhánh:** `feat/kien/q5-q6`

---

## 1. Tóm tắt

| Việc của TV3 | Trạng thái | Vị trí |
|---|---|---|
| EDA mục 3.2.4 (`sex`, `age`, `generation`, `HDI for year`) | Xong, đã vào `main` | `01_collection_exploration.ipynb` |
| Q5: code, phương pháp, 4 biểu đồ | Xong | `02_analysis.ipynb`, cell 6–23 |
| Q6: code, phương pháp, 3 biểu đồ | Xong | `03_ml_question.ipynb` |
| Kết quả và thảo luận Q5, Q6 | **Kiên đang viết** | `02_analysis.ipynb` cell 24; `03_ml_question.ipynb` cell 21 |
| Individual Reflection 3.5.4 | **Kiên đang viết** | |
| `LLM_USAGE.md` mục 2.3 | Có dòng 01–06, sẽ thêm dòng cho lần rà soát này | |
| Merge `feat/kien/q5-q6` vào `main` | **Chưa**, sẽ mở PR | |

---

## 2. Kết quả rà soát

### 2.1. Q5 so với yêu cầu non-ML (cần ít nhất 2 tiêu chí D)

| Tiêu chí | Cách làm trong Q5 | Đạt |
|---|---|---|
| D1 Ghép dữ liệu | Ghép `country_region.csv` (World Bank); 27,660 → 27,660 dòng; liệt kê 11 tên không khớp và bảng ánh xạ | ✅ |
| D2 Thời gian | Ma trận quốc gia × năm (Hình Q5.1); tách thiếu theo năm và thiếu theo nước | ✅ |
| D3 Biến phái sinh | `is_missing_hdi`, `missing_type`, Bias% | ✅ |
| D4 Kiểm soát biến nhiễu | Bias% theo tuổi, giới, giai đoạn, khu vực | ✅ |
| D5 Bất định | Mann-Whitney U, Kolmogorov-Smirnov, cluster bootstrap 1,000 lần | ✅ |
| D6 Độ vững | Bỏ Nga, bỏ 9 nước không bao giờ có HDI, chỉ nước có độ phủ > 80%, dùng trung vị | ✅ |

### 2.2. Q6 so với 6 yêu cầu ML

| Yêu cầu | Cách làm trong Q6 | Đạt |
|---|---|---|
| 1. Người dùng, đặc trưng có tại thời điểm dự báo, cột bị loại | Cơ quan y tế; đặc trưng chỉ từ năm t và t−1; loại HDI, `generation`, năm 2016, mọi cột năm t+1 | ✅ |
| 2. Chia theo thời gian | Train năm đích 1990–2010 (18,108 mẫu), test 2011–2015 (4,428 mẫu) | ✅ |
| 3. ≥ 2 mô hình + baseline, tiền xử lý trong `Pipeline` | Ridge, Random Forest, persistence; `ColumnTransformer` trong `Pipeline` | ✅ |
| 4. CV chỉ trên train, test một lần, biện luận thước đo | `TimeSeriesSplit` 5 fold trên danh sách năm; test một lần; MAE chính, RMSE phụ | ✅ |
| 5. Phân tích lỗi | Theo tuổi, giới, mức tỷ lệ năm t, nước chỉ có trong test; 5 mẫu sai lớn nhất | ✅ |
| 6. Giải thích mô hình và trả lời câu hỏi | Permutation importance xong; câu trả lời nằm trong ô thảo luận đang viết | ⏳ |

### 2.3. Yêu cầu chung của mục 3.4

Cả Q5 và Q6 đã có:
- mô tả tiền xử lý bằng Markdown;
- số dòng sau mỗi bước làm đổi dữ liệu (`check_row_count`);
- giải thích phương pháp;
- ít nhất 2 biểu đồ có tiêu đề, trục, đơn vị, chú thích.

Còn thiếu phần trả lời bằng số liệu cụ thể (ô thảo luận).

### 2.4. Chạy thử bản ghép với nhánh của Huy

- `feat/kien/q5-q6` và `feature/analysis-huy` cùng sửa `02_analysis.ipynb`, nhưng `git merge-tree` cho thấy **ghép được, không xung đột**.
- Bản ghép được chạy trên một bản sao riêng: cả 3 notebook Restart & Run All trong `min_ds-env` (pandas 2.1.1, scikit-learn 1.3.1) đều **0 lỗi, 0 cảnh báo**.
  - Thời gian chạy: `01` mất 10 giây, `02` mất 61 giây, `03` mất 137 giây.
  - Số liệu Q5 (Bias% −12.24%) và Q6 (test MAE 2.065) giữ nguyên sau khi ghép.

---

## 3. Nhờ các thành viên khác xem

| # | Vấn đề | Đề xuất | Người |
|---|---|---|---|
| 1 | `feat/kien/q5-q6` chưa vào `main` | Em mở PR; Huy review và merge cùng `feature/analysis-huy`, rồi chạy lại cả 3 notebook trên `main` | Huy |
| 2 | README, Key finding 4, ghi "cải thiện **đáng kể** MAE… nhận diện sớm các phân nhóm có nguy cơ cao". Kết quả test thật là MAE giảm 6.68% (2.213 → 2.065), RMSE giảm 17.04%; mô hình kém hơn persistence ở nhóm có tỷ lệ năm t < 5 và nhóm 5-14 tuổi | Em gửi lại câu chữ có số liệu sau khi viết xong thảo luận Q6 | Huy |
| 3 | README chưa có key finding của Q5 | Em gửi sau khi viết xong thảo luận Q5 | Huy |
| 4 | Khi chạy bằng `nbconvert`, biểu đồ đầu tiên của notebook `01` (cell 11) và `02` (cell 10, Q1) chỉ in `<Figure ...>`, không có hình | Thêm `%matplotlib inline` vào cell import chung | Huy |
| 5 | Con số "~69.6%" vẫn còn ở cell nhận xét đầu của notebook `01` và trong kế hoạch (đúng là 69.94%) | Sửa lại | Huy |
| 6 | README ghi tên TV3 theo kiểu placeholder `*[Nguyễn Đỗ Bảo Kiên]*`, `*[24122039]*` | Bỏ `*[ ]*` | Huy |
| 7 | Thư mục `Docs/` không có trong cấu trúc repo mà đề yêu cầu | Nhóm quyết định giữ hay xóa trước khi khóa bài | Cả nhóm |
| 8 | `slides.pdf` chưa có | Em gửi các hình `data/processed/tv3_q5_*.png`, `tv3_q6_*.png` và số liệu chính của Q5, Q6 | TV2 |

---

## 4. Việc còn lại

- [ ] Kiên viết thảo luận Q5 (cell 24) và Q6 (cell 21).
- [ ] Kiên viết Individual Reflection 3.5.4.
- [ ] Kiên thêm vào `LLM_USAGE.md` dòng ghi lần rà soát này.
- [ ] Kiên mở PR `feat/kien/q5-q6` → `main`: https://github.com/24122039Kien/HCMUS_HKD_program_for_data_scientists/compare/main...feat/kien/q5-q6
- [ ] Huy merge các nhánh, chạy lại 3 notebook trên `main`.
- [ ] Cả nhóm: mock defense (26/11), khóa bài trước 23:59 ngày 27/11.

---

## 5. Ghi chú về dùng AI

Lần rà soát này do Claude Code thực hiện theo yêu cầu của em: đối chiếu Q5, Q6 với đề, chạy thử bản ghép và soạn báo cáo. Chi tiết sẽ được ghi ở `LLM_USAGE.md`, mục 2.3.
