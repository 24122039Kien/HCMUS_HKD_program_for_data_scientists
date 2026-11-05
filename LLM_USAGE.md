# NHẬT KÝ SỬ DỤNG CÔNG CỤ AI / LLM (LLM_USAGE.md)
## MÔN HỌC: CSC17104 – LẬP TRÌNH CHO KHOA HỌC DỮ LIỆU
**Đề tài:** Phân tích và Dự báo Tỷ lệ Tự tử Toàn cầu (Suicide Rates Overview 1985–2016)  
**Nhóm:** 3 thành viên

---

## 1. CAM KẾT LIÊM CHÍNH HỌC THUẬT (ACADEMIC INTEGRITY)
Nhóm cam kết tuân thủ đúng quy định tại **Mục 6** của đề cương đồ án:
- Chỉ sử dụng các công cụ LLM (ChatGPT, Claude, Gemini, Copilot...) như một **gia sư (tutor)** hỗ trợ: giải thích khái niệm, gỡ lỗi cú pháp thư viện, tối ưu hóa code và gợi ý phương pháp thống kê.
- Tuyệt đối **không sử dụng LLM để viết thay** phần phân tích insight, rút ra kết luận định lượng, hoặc viết phần phản tư cá nhân (*Individual Reflection*).
- Mọi lần trao đổi quan trọng đều được ghi nhận trung thực và minh bạch theo từng thành viên bên dưới.

---

## 2. NHẬT KÝ SỬ DỤNG AI THEO TỪNG THÀNH VIÊN

### 2.1. Thành viên 1: [Điền Họ và Tên - MSSV]
*Phụ trách: Quản trị Git, Mục 3.1 Data Collection, EDA thời gian/không gian, Q1 & Q2, `src/utils.py`*

| STT | Ngày | Công cụ AI | Yêu cầu / Câu hỏi đã gửi (Prompt) | Kết quả nhận được & Cách áp dụng, chỉnh sửa |
| :---: | :---: | :---: | :--- | :--- |
| **01** | 03/11 | Antigravity (Claude / Gemini) | *"Lập kế hoạch chi tiết đồ án Khoa học Dữ liệu cho bộ dữ liệu Suicide Rates Overview theo rubric đề bài CSC17104."* | Nhận khung kế hoạch tổng thể; nhóm họp thảo luận, chốt danh sách 6 câu hỏi và ma trận phân công công việc. |
| **02** | 05/11 | Antigravity (Claude / Gemini) | *"Kiểm tra tính đầy đủ của 6 tiêu chí D1-D6 và 6 yêu cầu Machine Learning theo file PDF đề bài."* | Phát hiện câu hỏi Non-ML ban đầu thiếu tiêu chí D1. Bổ sung D1 vào Q5 bằng cách ghép file `country_region.csv`. |
| **03** | *[Điền]* | *[Tên AI]* | *[Ví dụ: Cách kiểm tra tính duy nhất của khóa country-year-sex-age]* | *[Ví dụ: Dùng hàm duplicated(), viết vào Mục 3.2]* |
| **04** | *[Điền]* | *[Tên AI]* | *[Ví dụ: Thuật toán Cluster Bootstrap tính 95% CI cho Q2]* | *[Ví dụ: Tham khảo code lấy mẫu theo cụm, viết vào src/utils.py]* |

---

### 2.2. Thành viên 2: [Điền Họ và Tên - MSSV]
*Phụ trách: EDA nhóm cột số & kinh tế, Chuẩn hóa đồ thị `src/visualization.py`, Q3 & Q4, Mục 3.5 & `slides.pdf`*

| STT | Ngày | Công cụ AI | Yêu cầu / Câu hỏi đã gửi (Prompt) | Kết quả nhận được & Cách áp dụng, chỉnh sửa |
| :---: | :---: | :---: | :--- | :--- |
| **01** | *[Điền]* | *[Tên AI]* | *[Ví dụ: Cách xử lý chuỗi có dấu phẩy ở cột GDP sang số nguyên]* | *[Ví dụ: Dùng str.replace(',', '').astype(int), áp dụng vào EDA cột số]* |
| **02** | *[Điền]* | *[Tên AI]* | *[Ví dụ: Công thức tính Tỷ lệ chuẩn hóa tuổi trực tiếp (ASR) theo dân số chuẩn WHO]* | *[Ví dụ: Hiểu công thức toán học, tự lập trình hàm calculate_asr trong src/utils.py]* |
| **03** | *[Điền]* | *[Tên AI]* | *[Ví dụ: Cách thiết lập Seaborn style chuẩn học thuật cho đồ thị]* | *[Ví dụ: Đưa cấu hình font chữ, DPI vào src/visualization.py]* |

---

### 2.3. Thành viên 3: [Điền Họ và Tên - MSSV]
*Phụ trách: EDA nhân khẩu học & thiếu HDI, Q5, Machine Learning Pipeline Q6, `LLM_USAGE.md` & Mock Defense*

| STT | Ngày | Công cụ AI | Yêu cầu / Câu hỏi đã gửi (Prompt) | Kết quả nhận được & Cách áp dụng, chỉnh sửa |
| :---: | :---: | :---: | :--- | :--- |
| **01** | *[Điền]* | *[Tên AI]* | *[Ví dụ: Cách vẽ Missingness Heatmap theo trục thời gian cho cột HDI]* | *[Ví dụ: Dùng sns.heatmap(df.pivot_table(index='country', columns='year', values='is_missing')), áp dụng vào EDA]* |
| **02** | *[Điền]* | *[Tên AI]* | *[Ví dụ: Thiết kế scikit-learn Pipeline kết hợp SimpleImputer và OneHotEncoder cho Q6]* | *[Ví dụ: Tham khảo cấu trúc ColumnTransformer, áp dụng vào notebook 03]* |
| **03** | *[Điền]* | *[Tên AI]* | *[Ví dụ: Cách dùng TimeSeriesSplit chia tập train/test theo năm để chống rò rỉ dữ liệu]* | *[Ví dụ: Áp dụng vào phần Cross-Validation của Q6]* |

---
*Bảng nhật ký này được các thành viên cập nhật liên tục và độc lập trong suốt quá trình làm đồ án.*
