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

### 2.3. Thành viên 3: Nguyễn Đỗ Bảo Kiên - 24122039
*Phụ trách: EDA nhân khẩu học & thiếu HDI, Q5, Machine Learning Pipeline Q6, `LLM_USAGE.md` & Mock Defense*

| STT | Ngày | Công cụ AI | Yêu cầu / Câu hỏi đã gửi (Prompt) | Kết quả nhận được & Cách áp dụng, chỉnh sửa |
| :---: | :---: | :---: | :--- | :--- |
| **01** | 08/11 | Claude Code (Claude Opus 5.5) | *"Hãy đọc toàn bộ đề bài, kế hoạch phân công và repo hiện tại của đồ án; tóm tắt yêu cầu và tiến độ, đồng thời kiểm tra sơ bộ trên dữ liệu thật để chỉ ra các điểm chưa nhất quán trước khi tôi bắt đầu phần việc của TV3."*  | AI tóm tắt yêu cầu đề bài, kế hoạch nhóm và tiến độ repo, đồng thời chạy kiểm tra trên dữ liệu thật. Phát hiện: HDI thiếu 69.94% (README và kế hoạch đang ghi ~69.6%); năm 2016 thiếu nhóm tuổi 5-14; `generation` suy ra được từ (`year`, `age`); cell 13–14 của mục 3.2.2 có bảng bị NaN và số liệu nhận xét không khớp output. Em dùng kết quả này để chuẩn bị phần EDA của mình và báo lại cho nhóm khi review chéo. |
| **02** | 08/11 | Claude Code (Claude Opus 5.5) | *"Thực hiện phần EDA của TV3 theo kế hoạch nhóm: (1) kiểm tra nhãn, độ cân bằng của `sex`, `age` và tính đủ 12 phân nhóm mỗi (country, year); (2) kiểm tra `generation` có phải biến dư thừa so với (`year`, `age`); (3) phân tích mức độ và cơ chế thiếu của `HDI for year`; (4) đếm số cặp năm liên tiếp $(t, t+1)$ đủ điều kiện cho Q6. Viết vào mục 3.2.4 của notebook và chạy lại để kiểm chứng số liệu."* | AI viết code và phần nhận xét của mục 3.2.4 (5 phần a–e, 5 biểu đồ), chạy lại toàn bộ notebook trong môi trường conda để kiểm chứng, và đối chiếu mọi con số trong nhận xét với output. Phần này được đưa vào notebook trên nhánh `feature/eda-kien`; các cell của TV1 giữ nguyên. AI soạn kèm file ghi chú giải thích từng bước và câu tự kiểm tra (không đưa vào repo), em dùng để ôn và tự giải thích được code khi vấn đáp. |
| **03** | 08/11 | Claude Code (Claude Opus 5.5) | *"`git push` bị GitHub từ chối với lỗi GH007 do commit chứa email cá nhân đang đặt ở chế độ riêng tư. Giải thích nguyên nhân và đề xuất cách khắc phục mà không làm lộ email."* | AI giải thích nguyên nhân và đưa 2 phương án. Em chọn dùng email noreply của GitHub cho repo này; AI ký lại 2 commit bằng email noreply rồi push nhánh `feature/eda-kien` thành công. |


---
*Bảng nhật ký này được các thành viên cập nhật liên tục và độc lập trong suốt quá trình làm đồ án.*
