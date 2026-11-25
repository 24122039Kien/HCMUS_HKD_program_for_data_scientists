# Bàn giao phần việc của Đăng (TV2)

Ngày kiểm tra: 23/11/2026. Nhánh `feature/q3-q4` dựa trên `main@1e05dfd` và lấy thêm bốn commit của TV3 đến `8f98551` để chạy Q5–Q6 cùng bài nhóm.

| Giai đoạn | Sản phẩm | Vị trí |
| --- | --- | --- |
| 1 · Khám phá dữ liệu | Thống kê năm biến số, kiểm tra số ca/dân số, sai số làm tròn, phân phối, ngoại lai, tính nhất quán GDP. Đã sửa cách tra kiểu ban đầu của GDP có khoảng trắng trong tiêu đề CSV. | [Notebook 01, mục 3.2.3](../notebooks/01_collection_exploration.ipynb) |
| 2 · Đặc tả và xử lý | Q3 lấy sai phân đúng năm lịch, phân ba nhóm GDP. Q4 dùng cùng mẫu quốc gia và hai bộ trọng số cho dân số từ 5 tuổi. | [Notebook Q3–Q4](../notebooks/02_analysis_q3_q4.ipynb) |
| 3 · Phân tích và tổng hợp | Bốn biểu đồ, bảng kiểm tra độ vững, phân rã thay đổi tỷ lệ thô, đối chiếu sáu câu hỏi và bản nháp phản tư kỹ thuật. | [Notebook 02, Q3, Q4 và mục 3.5](../notebooks/02_analysis.ipynb) |
| 4 · Trình bày | Chín trang, ba phần 5 phút. TV1 trình bày dữ liệu và Q1–Q2, TV2 trình bày GDP và chuẩn hóa tuổi, TV3 trình bày HDI và dự báo. Mốc thời gian nằm ở chân mỗi trang. | [Slide báo cáo](../slides.pdf) |

## Đối chiếu số liệu và rà soát chéo

- Ghép Q3 trên khóa nước và năm lịch cho 2.148 cặp một năm và 2.028 cặp hai năm. Một phép thử có năm gián đoạn xác nhận thuật toán bỏ cặp sai độ trễ.
- Với cùng dữ liệu, phép nội suy ngưỡng phân vị trong hai phiên bản pandas xếp một nước sát ngưỡng sang hai nhóm GDP khác nhau. Mã dùng thứ hạng thực nghiệm để cố định hai ngưỡng. Ba nhóm có 655, 735 và 758 cặp năm.
- Q4 giữ 7.056 dòng của 49 nước, đủ 6 năm trong mỗi giai đoạn. Cả 98 kết quả nước–giai đoạn được so với hai hàm độc lập `calculate_aggregated_rate` và `calculate_asr` trong `src/utils.py`. Hai thành phần cơ cấu tuổi và tỷ lệ riêng cộng đúng bằng thay đổi tỷ lệ thô.
- Q5 của TV3 đối chiếu bảng vùng trước và sau chuẩn hóa tên nước. Ước lượng chênh lệch khi chỉ giữ dòng có HDI là −12,24%, khoảng bootstrap 95% bao gồm 0. Khi trình bày cần giữ cả khoảng này và phạm vi 10 năm có HDI.
- Q6 ghép t−1 và t+1 theo năm lịch trong cùng nhóm. Các fold và tập test được tách theo năm đích. Biến đích và năm đích nằm ngoài danh sách đặc trưng. Khi đổi dữ liệu, đoạn chọn mô hình cuối luôn chọn giữa các mô hình học máy sau khi bỏ hàng persistence khỏi bảng xếp hạng. Cần đối chiếu lại baseline nếu dùng bộ dữ liệu khác.
- Nhánh hiện có chỉ chứa tiêu đề phần Q1–Q2 của TV1. Các bảng ở mục 3.5 và slide Q1–Q2 là phép tính riêng của TV2. Khi TV1 ghép kết quả chính thức, cần đối chiếu định nghĩa mẫu, hệ số và khoảng tin cậy.
- Nhật ký AI ghi rõ nguồn bản nháp nhận xét và phản tư. TV2 duyệt nội dung cá nhân trước khi chốt bài. Buổi trình bày thử, phê duyệt PR và nộp bài là các mốc của nhóm.

## Dữ liệu để tái lập

`data/raw/master.csv` tải từ [bộ dữ liệu Kaggle](https://www.kaggle.com/datasets/russellyates88/suicide-rates-overview-1985-to-2016), gồm 27.820 dòng và 12 cột. SHA-256: `e1b9f9bc2552933248d66296bd52f4987f4b9841a897b38eec49a2bf4f7eaba6`. Bảng `data/raw/country_region.csv` đến từ nhánh TV3. Trọng số tuổi dùng [bảng WHO 2000–2025 do NCI/SEER công bố](https://seer.cancer.gov/stdpopulations/world.who.html).


## Biên bản chạy lại trên Windows

Môi trường Conda mới dùng đúng `environment.yml`. Conda cài xong các gói chính nhưng launcher trên máy gặp lỗi ở bước kích hoạt đường dẫn có khoảng trắng. Gói pip cuối cùng được cài trực tiếp bằng Python của chính môi trường đó (`python -m pip install "pdfplumber>=0.10.0"`). Kiểm tra `python -m pip check` thành công.

Mỗi notebook khởi động một kernel mới trong thư mục `notebooks/`. Trình kiểm tra đối chiếu đường dẫn Python của kernel với môi trường vừa tạo, kiểm tra mọi ô code đã chạy và dò output lỗi. Thứ tự chạy: 01, 02, 03, rồi notebook Q3–Q4 độc lập.

| Notebook | Ô code đã chạy | Thời gian | Kết quả |
| --- | ---: | ---: | --- |
| `01_collection_exploration.ipynb` | 30 | 44.3 giây | Đạt |
| `02_analysis.ipynb` | 18 | 210.6 giây | Đạt |
| `03_ml_question.ipynb` | 11 | 544.6 giây | Đạt |
| `02_analysis_q3_q4.ipynb` | 7 | 16.3 giây | Đạt |

Phiên bản đã kiểm tra: numpy 2.2.6, pandas 2.3.3, scipy 1.15.2, matplotlib 3.10.9, seaborn 0.13.2, scikit-learn 1.7.2, nbclient 0.11.0, pdfplumber 0.11.10.

Bảng Q6 từ lần chạy mới (MAE và RMSE theo ca/100.000):

```text
MAE    RMSE
Persistence (baseline)               2.213   5.844
Random Forest – dự báo mức thay đổi  2.065   4.848
Cải thiện (%)                        6.683  17.040
```

Sau khi Q6 trả kết quả, tiến trình phụ joblib báo KeyError khi dọn thư mục tạm trên Windows. Cả 11 ô code đã hoàn thành, ba hình Q6 đã xuất và các chỉ số test trùng với số liệu TV3 công bố ở độ chính xác ba chữ số thập phân.
