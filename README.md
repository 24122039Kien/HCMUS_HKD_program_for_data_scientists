# PHÂN TÍCH VÀ DỰ BÁO TỶ LỆ TỰ TỬ TOÀN CẦU (SUICIDE RATES OVERVIEW 1985–2016)
## ĐỒ ÁN CUỐI KỲ MÔN HỌC: CSC17104 – LẬP TRÌNH CHO KHOA HỌC DỮ LIỆU
**Khoa Công nghệ Thông tin – Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM (FIT-HCMUS)**

---

## 1. THÔNG TIN NHÓM VÀ PHÂN CÔNG TRÁCH NHIỆM

### 1.1. Danh sách thành viên
| STT | Họ và Tên | MSSV | Vai trò chính | Email |
| :---: | :--- | :---: | :--- | :--- |
| 1 | Phan Nguyễn Gia Huy | 24122035 | **Trưởng nhóm:** Quản trị Git/Repo, Data Collection (3.1), EDA Overview & Không gian–thời gian, phụ trách **Q1 & Q2**, `src/utils.py`. | fanzahuy1472@gmail.com |
| 2 | Đăng *(Chờ cập nhật họ tên)* | *[Điền MSSV]* | **Thành viên:** EDA cột số & kinh tế, Chuẩn hóa tuổi (ASR), Chuẩn hóa đồ thị `src/visualization.py`, phụ trách **Q3 & Q4**, Mục 3.5 & `slides.pdf`. | *[Email]* |
| 3 | Nguyễn Đỗ Bảo Kiên | 24122039 | **Thành viên:** EDA nhân khẩu học & thiếu HDI, Ghép dữ liệu ngoài (D1), Xây dựng Machine Learning Pipeline **Q6**, phụ trách **Q5 & Q6**, `LLM_USAGE.md` & Mock Defense. | *[Email]* |

### 1.2. Quyền sở hữu 6 câu hỏi nghiên cứu (Question Ownership)
* **Q1 (Huy):** Xu hướng tỷ lệ tử vong do tự tử toàn cầu: Mẫu cố định (Fixed Cohort) vs Mẫu đầy đủ (All Available Countries) *(D2, D3, D6)*.
* **Q2 (Huy):** Chênh lệch tỷ lệ tử vong Nam – Nữ theo 6 độ tuổi và Khoảng tin cậy Cluster Bootstrap 95% CI *(D3, D4, D5)*.
* **Q3 (Đăng):** Mối liên hệ giữa biến động GDP bình quân đầu người và Tỷ lệ tử vong trong cùng quốc gia *(D2, D3, D4, D6)*.
* **Q4 (Đăng):** Tác động của già hóa dân số: So sánh Tỷ lệ thô và Tỷ lệ chuẩn hóa theo độ tuổi trực tiếp (ASR) *(D2, D3, D4, D6)*.
* **Q5 (Kiên):** Khảo sát dữ liệu thiếu của HDI và sai lệch ước lượng theo độ tuổi & vùng địa lý *(D1, D2, D3, D4, D5, D6)*.
* **Q6 (Kiên - Machine Learning):** Hệ thống cảnh báo sớm: Dự báo tỷ lệ tử vong năm $t+1$ cấp độ nhóm không rò rỉ dữ liệu *(Đạt chuẩn 6/6 tiêu chí ML)*.

---

## 2. MÔ TẢ BỘ DỮ LIỆU & NGUỒN GỐC (DATASET DESCRIPTION)

- **Tên bộ dữ liệu:** Suicide Rates Overview 1985 to 2016
- **Nguồn dữ liệu:** Được tổng hợp trên nền tảng [Kaggle](https://www.kaggle.com/datasets/russellyates88/suicide-rates-overview-1985-to-2016) từ 4 nguồn tổ chức uy tín:
  - World Health Organization (WHO) - Thống kê tự tử toàn cầu.
  - World Bank - Chỉ số phát triển thế giới và GDP.
  - United Nations Development Program (UNDP) - Chỉ số phát triển con người (HDI).
  - Bộ dữ liệu tiền thân trên Kaggle của tác giả Szamil (2017 - "Suicide in the Twenty-First Century") kế thừa việc phân loại thế hệ nhân khẩu học (`generation`) theo định nghĩa xã hội học phương Tây (Pew Research Center).
- **Quy mô:** 27,820 dòng, 12 cột, bao phủ 101 quốc gia trong giai đoạn 1985–2016.
- **Giấy phép (License):** World Bank Dataset Terms of Use (tương thích CC BY 4.0 - Dữ liệu mở cho phép sử dụng, phân tích và nghiên cứu học thuật kèm yêu cầu ghi công nguồn gốc).
- **Khai báo công trình tham khảo (Declare existing work - Bắt buộc theo đề bài):**
  - Nhóm có tham khảo một số phân tích mô tả sơ bộ từ notebook công khai trên Kaggle: [Global Suicide Analysis (1985-2016)](https://www.kaggle.com/code/pratyusha2005/global-suicide-analysis-1985-2016/notebook).
  - **Điểm khác biệt và đóng góp độc lập của nhóm:**
    1. Kế thừa việc khám phá các biến cơ bản, nhưng nhóm đã đi sâu vào xử lý các vấn đề chất lượng dữ liệu nghiêm trọng (loại bỏ thiên lệch chọn mẫu, phân tích cơ chế thiếu của HDI).
    2. Áp dụng kỹ thuật dịch tễ học chuyên sâu: **Chuẩn hóa trực tiếp theo tuổi (ASR)** và **Cluster Bootstrap 95% CI**.
    3. Xây dựng bài toán **Machine Learning dự báo chuỗi thời gian cho năm $t+1$** với cơ chế chống rò rỉ dữ liệu tuyệt đối (Time-based split, scikit-learn Pipeline, Permutation Feature Importance), điều mà các notebook Kaggle trước đây không thực hiện.

---

## 3. CẤU TRÚC THƯ MỤC DỰ ÁN (PROJECT REPOSITORY STRUCTURE)

```text
suicide-rates-analysis/
├── .gitignore                           # Chặn commit file tạm, file lớn
├── README.md                            # Tài liệu chính của đồ án
├── environment.yml                      # Cấu hình môi trường Conda
├── LLM_USAGE.md                         # Nhật ký minh bạch sử dụng AI
├── slides.pdf                           # Slide báo cáo thuyết trình (15 phút)
├── data/
│   ├── raw/                             # master.csv, country_region.csv (không commit file lớn)
│   └── processed/                       # Dữ liệu sạch sau tiền xử lý
├── src/                                 # Mô-đun Python tái sử dụng
│   ├── __init__.py
│   ├── utils.py                         # Hàm tính toán: tỷ lệ gộp, ASR, bootstrap CI, kiểm tra dòng
│   ├── economy_age.py                   # Hàm xử lý sai phân GDP & chuẩn hóa tuổi ASR (Q3, Q4)
│   └── visualization.py                 # Chuẩn hóa style đồ thị Seaborn/Matplotlib
└── notebooks/
    ├── 01_collection_exploration.ipynb  # Mục 3.1 & 3.2: Thu thập & Khám phá EDA 12 cột
    ├── 02_analysis.ipynb                # Mục 3.3, 3.4 & 3.5: Phân tích 5 câu Non-ML & Tổng kết
    └── 03_ml_question.ipynb             # Mục 3.3 & 3.4: Bài toán Machine Learning Q6
```

---

## 4. HƯỚNG DẪN CÀI ĐẶT VÀ TÁI LẬP DỰ ÁN (REPRODUCIBILITY GUIDE)

Để chạy lại toàn bộ đồ án từ đầu trên môi trường sạch, vui lòng thực hiện tuần tự các bước sau trong Terminal / Anaconda Prompt:

### Bước 1: Clone repository
```bash
git clone https://github.com/24122039Kien/HCMUS_HKD_program_for_data_scientists.git
cd HCMUS_HKD_program_for_data_scientists
```

### Bước 2: Tạo và kích hoạt môi trường Conda
```bash
conda env create -f environment.yml
conda activate csc17104_suicide_rates
```

### Bước 3: Tải dữ liệu vào thư mục `data/raw/`
1. Tải tệp `master.csv` từ [Kaggle Suicide Rates Dataset](https://www.kaggle.com/datasets/russellyates88/suicide-rates-overview-1985-to-2016).
2. Đặt tệp vào đường dẫn: `data/raw/master.csv`.

### Bước 4: Chạy các Notebook theo đúng thứ tự
Khởi động Jupyter Lab hoặc Jupyter Notebook:
```bash
jupyter notebook
```
Chạy tuần tự thông qua lệnh **Kernel -> Restart & Run All**:
1. `notebooks/01_collection_exploration.ipynb`: Chạy thu thập và khám phá dữ liệu.
2. `notebooks/02_analysis.ipynb`: Chạy phân tích chuyên sâu 5 câu hỏi Non-ML và xem tổng kết.
3. `notebooks/03_ml_question.ipynb`: Huấn luyện mô hình, đánh giá trên test set và xem phân tích lỗi.

---

## 5. TÓM TẮT CÁC PHÁT HIỆN CHÍNH (KEY FINDINGS)
1. **Phát hiện 1 (Bẫy chọn mẫu - Q1):** Trong giai đoạn 1990–2015, tỷ lệ tự tử trên toàn bộ quốc gia nộp báo cáo (`All Available`, 62–89 nước/năm) giảm **-12.96%** (13.18 xuống 11.47 ca/100k dân). Tuy nhiên, khi theo dõi cùng tập **34 quốc gia liên tục (`Fixed Balanced Cohort`)**, mức giảm thực chất chỉ đạt **-6.18%** (12.86 xuống 12.07 ca/100k; và **-8.81%** trên `Relaxed Cohort` 50 nước) — cho thấy sự gia nhập của các nước có tỷ lệ thấp sau năm 2000 tạo ra ảo ảnh giảm nhanh hơn gấp đôi.
2. **Phát hiện 2 (Nghịch lý chênh lệch giới - Q2):** Trên **12,324 cặp** (99 quốc gia), toàn bộ 6 độ tuổi đều có 95% Cluster Bootstrap CI > 0. Người cao tuổi **75+** chịu mức *chênh lệch tuyệt đối* lớn nhất (**28.35 ca/100k**, 95% CI: [23.85, 32.97]), nhưng **nam thanh niên 25–34 tuổi** lại có *tỷ số tương đối* cao nhất (trung vị **4.19 lần**, tỷ số gộp **4.41 lần** so với nữ).
3. **Phát hiện 3 (Biến động GDP ngắn hạn - Q3):** Khi khử yếu tố cố định của từng quốc gia bằng sai phân bậc nhất trên **2,148 cặp năm liền kề** (96 nước), tăng trưởng GDP danh nghĩa có tương quan nghịch chu kỳ rất yếu với biến động tỷ lệ tự tử ($r = -0.0289$, $\rho = -0.0544$, độ dốc **-0.0449 ca/100k** cho mỗi +10% GDP), và gần như triệt tiêu ở nhóm thu nhập cao ($r = -0.0043$).
4. **Phát hiện 4 (Già hóa dân số che lấp cải thiện thực chất - Q4):** Trên **49 quốc gia** đủ dữ liệu giai đoạn 1995–2000 và 2010–2015, tỷ lệ thô giảm **-2.087 ca/100k** (14.515 xuống 12.428), trong khi **Tỷ lệ chuẩn hóa theo tuổi (WHO ASR)** giảm tới **-2.607 ca/100k** (13.858 xuống 11.252). Phân rã Kitagawa chỉ ra yếu tố già hóa (+4.61 điểm % nhóm 55+) đã kéo tỷ lệ thô tăng ngược **+0.809 ca/100k**, làm triệt tiêu 38.75% mức giảm rủi ro theo tuổi (-2.896 ca/100k).
5. **Phát hiện 5 & 6 (Thiếu dữ liệu HDI & Dự báo ML - Q5, Q6):** *(Sẽ cập nhật số liệu đối chiếu cuối cùng sau khi ghép hoàn chỉnh phần Q5 & Q6 từ nhánh `feat/kien/q5-q6`)*.

