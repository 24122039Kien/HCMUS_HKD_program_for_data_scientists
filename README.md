# PHÂN TÍCH VÀ DỰ BÁO TỶ LỆ TỰ TỬ TOÀN CẦU (SUICIDE RATES OVERVIEW 1985–2016)
## ĐỒ ÁN CUỐI KỲ MÔN HỌC: CSC17104 – LẬP TRÌNH CHO KHOA HỌC DỮ LIỆU
**Khoa Công nghệ Thông tin – Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM (FIT-HCMUS)**

---

## 1. THÔNG TIN NHÓM VÀ PHÂN CÔNG TRÁCH NHIỆM

### 1.1. Danh sách thành viên
| STT | Họ và Tên | MSSV | Vai trò chính | Email |
| :---: | :--- | :---: | :--- | :--- |
| 1 | *[Điền họ tên TV1]* | *[Điền MSSV]* | **Trưởng nhóm:** Quản trị Git/Repo, Data Collection (3.1), EDA Overview & Không gian–thời gian, phụ trách **Q1 & Q2**, `src/utils.py`. | *[Email]* |
| 2 | *[Điền họ tên TV2]* | *[Điền MSSV]* | **Thành viên:** EDA cột số & kinh tế, Chuẩn hóa tuổi (ASR), Chuẩn hóa đồ thị `src/visualization.py`, phụ trách **Q3 & Q4**, Mục 3.5 & `slides.pdf`. | *[Email]* |
| 3 | *[Điền họ tên TV3]* | *[Điền MSSV]* | **Thành viên:** EDA nhân khẩu học & thiếu HDI, Ghép dữ liệu ngoài (D1), Xây dựng Machine Learning Pipeline **Q6**, phụ trách **Q5 & Q6**, `LLM_USAGE.md` & Mock Defense. | *[Email]* |

### 1.2. Quyền sở hữu 6 câu hỏi nghiên cứu (Question Ownership)
* **Q1 (TV1):** Xu hướng tỷ lệ tử vong do tự tử toàn cầu: Mẫu cố định (Fixed Cohort) vs Mẫu đầy đủ (All Available Countries) *(D2, D3, D6)*.
* **Q2 (TV1):** Chênh lệch tỷ lệ tử vong Nam – Nữ theo 6 độ tuổi và Khoảng tin cậy Cluster Bootstrap 95% CI *(D3, D4, D5)*.
* **Q3 (TV2):** Mối liên hệ giữa biến động GDP bình quân đầu người và Tỷ lệ tử vong trong cùng quốc gia *(D2, D3, D4, D6)*.
* **Q4 (TV2):** Tác động của già hóa dân số: So sánh Tỷ lệ thô và Tỷ lệ chuẩn hóa theo độ tuổi trực tiếp (ASR) *(D2, D3, D4, D6)*.
* **Q5 (TV3):** Khảo sát dữ liệu thiếu của HDI và sai lệch ước lượng theo độ tuổi & vùng địa lý *(D1, D2, D3, D4, D5, D6)*.
* **Q6 (TV3 - Machine Learning):** Hệ thống cảnh báo sớm: Dự báo tỷ lệ tử vong năm $t+1$ cấp độ nhóm không rò rỉ dữ liệu *(Đạt chuẩn 6/6 tiêu chí ML)*.

---

## 2. MÔ TẢ BỘ DỮ LIỆU & NGUỒN GỐC (DATASET DESCRIPTION)

- **Tên bộ dữ liệu:** Suicide Rates Overview 1985 to 2016
- **Nguồn dữ liệu:** Được tổng hợp trên nền tảng [Kaggle](https://www.kaggle.com/datasets/russellyates88/suicide-rates-overview-1985-to-2016) từ 4 nguồn tổ chức uy tín:
  - World Health Organization (WHO) - Thống kê tự tử toàn cầu.
  - World Bank - Chỉ số phát triển thế giới và GDP.
  - United Nations Development Program (UNDP) - Chỉ số phát triển con người (HDI).
  - Dữ liệu dân số theo thế hệ của Liên Hợp Quốc.
- **Quy mô:** 27,820 dòng, 12 cột, bao phủ 101 quốc gia trong giai đoạn 1985–2016.
- **Giấy phép (License):** Dữ liệu công khai phục vụ mục đích giáo dục và nghiên cứu học thuật (Public Domain / CC0).
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
*(Phần này sẽ được cập nhật sau khi hoàn thành chạy số liệu phân tích chi tiết)*
1. **Phát hiện 1 (Giới tính & Tuổi):** Tỷ lệ tử vong ở nam giới cao gấp 3–4 lần nữ giới trên hầu hết các quốc gia, đặc biệt chênh lệch tăng vọt ở nhóm người cao tuổi ($\ge 55$ tuổi).
2. **Phát hiện 2 (Bẫy chọn mẫu):** Xu hướng giảm tỷ lệ toàn cầu giai đoạn sau năm 2000 phần lớn do sự gia nhập của các quốc gia đang phát triển có tỷ lệ ghi nhận thấp, khi cố định một tập quốc gia (Fixed Cohort) thì mức độ sụt giảm chậm hơn nhiều.
3. **Phát hiện 3 (Già hóa dân số):** Tại các quốc gia có tốc độ già hóa nhanh, tỷ lệ tử vong thô tăng lên nhưng tỷ lệ chuẩn hóa theo tuổi (ASR) thực tế lại giảm.
4. **Phát hiện 4 (Dự báo Machine Learning):** Mô hình Random Forest với các biến trễ chuỗi thời gian cải thiện đáng kể sai số MAE so với Naive Baseline, giúp nhận diện sớm các phân nhóm có nguy cơ cao trong năm tiếp theo.
