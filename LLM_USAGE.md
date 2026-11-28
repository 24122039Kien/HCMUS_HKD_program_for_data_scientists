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

### 2.1. Thành viên 1: Phan Nguyễn Gia Huy - 24122035
*Phụ trách: Quản trị Git, Mục 3.1 Data Collection, EDA thời gian/không gian, Q1 & Q2, `src/utils.py`*

| STT | Ngày | Công cụ AI | Yêu cầu / Câu hỏi đã gửi (Prompt) | Kết quả nhận được & Cách áp dụng, chỉnh sửa |
| :---: | :---: | :---: | :--- | :--- |
| **01** | 03/11 | Antigravity (Claude / Gemini) | *"Lập kế hoạch chi tiết đồ án Khoa học Dữ liệu cho bộ dữ liệu Suicide Rates Overview theo rubric đề bài CSC17104 và thiết kế cấu trúc repo chuẩn."* | Nhận khung kế hoạch 4 giai đoạn và cây thư mục chuẩn; nhóm họp thảo luận, chốt danh sách 6 câu hỏi nghiên cứu, thiết lập Git repo, `.gitignore` và `environment.yml`. |
| **02** | 05/11 | Antigravity (Claude / Gemini) | *"Kiểm tra tính đầy đủ của Mục 3.1 (License, Declare existing work), 6 tiêu chí chiều sâu D1–D6 và 6 yêu cầu Machine Learning theo file PDF đề bài."* | Phát hiện bộ câu hỏi Non-ML ban đầu thiếu tiêu chí D1; cùng nhóm bổ sung D1 vào Q5 bằng file `country_region.csv` và hoàn thiện Mục 3.1 chuẩn CC BY 4.0. |
| **03** | 06–09/11 | Antigravity (Claude / Gemini) | *"Hướng dẫn kiểm tra tính duy nhất khóa chính `(country, year, sex, age)`, tính nhất quán của `country-year`, lập bảng độ phủ thời gian và thiết kế module `src/utils.py`."* | Tự viết và chạy code kiểm tra 0 dòng trùng khóa, phát hiện năm 2016 chỉ có 16 nước và thiếu nhóm tuổi; viết hàm `check_row_count` và `calculate_aggregated_rate` vào `src/utils.py` để tránh Simpson's Paradox. |
| **04** | 14–23/11 | Antigravity (Claude / Gemini) | *"Giải thích bản chất thống kê của Selection Bias, phương pháp lọc Fixed Balanced Cohort (34 nước liên tục) vs Relaxed Cohort (D6) cho Q1 và lý giải cú sốc Đông Âu giai đoạn 1990–1995."* | Hiểu rõ sự khác biệt giữa xu hướng giả trên mẫu gộp (-12.96%) và xu hướng thực trên 34 nước (-6.18%); tự kiểm chứng với ngưỡng nới lỏng 50 nước (-8.81%) và hoàn thiện 3 biểu đồ Q1. |
| **05** | 23–26/11 | Antigravity (Claude / Gemini) | *"Giải thích chi tiết thuật toán Non-parametric Cluster Bootstrap (lấy mẫu lại 99 cụm quốc gia × 1,000 lần), cách đọc Forest Plot / Boxplot và lý giải nghịch lý tuyệt đối (75+) vs tương đối (25–34) ở Q2."* | Nắm vững cơ chế mô phỏng độ bất định bằng Cluster Bootstrap và cách triệt tiêu biến nhiễu qua Paired Design (D4); tự sửa lỗi bố cục legend đè chữ trên Hình 2.1 và diễn đạt lại phần giải thích theo hướng học thuật. |
| **06** | 25/11 | Antigravity (Claude / Gemini) | *"Hỗ trợ viết script đối chiếu toàn bộ con số nhận xét Markdown với kết quả chạy code thực tế trong `01_collection_exploration.ipynb` và `02_analysis.ipynb`."* | Phát hiện và tự sửa các sai lệch số liệu (cập nhật tỷ lệ thiếu HDI 69.94%, độ phủ 77–89 nước/năm, 31 nước $\ge 30$ năm, xử lý lỗi lệch index gây `NaN` bảng tổng hợp ở `01` và số liệu Q1/Q2 giai đoạn 1990–2015). |
| **07** | 26–27/11 | Antigravity (Claude / Gemini) | *"Hướng dẫn rà soát nhánh Git của TV2, TV3 (`feature/q3-q4`, `feat/kien/q5-q6`), tích hợp riêng phần Q3–Q4 vào `02_analysis.ipynb` tránh xung đột và kiểm tra lại chuẩn cấu trúc nộp bài."* | Kiểm tra lịch sử commit và diff của các thành viên, tách lọc tích hợp đúng Q3–Q4 + `src/economy_age.py` + `slides.pdf` mà không dính file dư thừa; đồng bộ khung trình bày 4 bước cho Q1–Q4 và lập checklist rà soát cho TV3. |
| **08** | 27/11 | Antigravity (Claude / Gemini) | *"Kiểm tra lại notebook 01, chạy benchmark tìm nguyên nhân chạy chậm, sửa lỗi hiển thị LaTeX/dtype và dựng khung chuẩn cho Mục 3.5."* | Sửa lỗi tra cứu cột `' gdp_for_year ($) '` (`str -> int64`), thêm `%matplotlib inline`, sửa lỗi tương quan GDP (`+0.060`/`+0.188`) và công thức `\times` ở `01`; kiểm tra chạy trọn vẹn 30/30 cell `01` và 19/19 cell `02` không lỗi, sau đó tự rà soát lại số liệu và viết lại phần phản tư cá nhân 3.5.4a. |

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
