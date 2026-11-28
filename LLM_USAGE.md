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

### 2.2. Thành viên 2: Phạm Hoàng Hải Đăng - 24122030
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
| **04** | 23/11 | Claude Code (Claude Opus 5.5) | *"Hiện tại việc của tôi đang còn những sprints nào vậy?"* | AI đối chiếu kế hoạch nhóm, `Docs/report01.md` và lịch sử Git, liệt kê các việc giai đoạn 2–3 và 4 của TV3 còn thiếu (Q5, Q6, Individual Reflection, `LLM_USAGE.md`, mock defense). Em dùng danh sách này để sắp thứ tự làm việc. |
| **05** | 23/11 | Claude Code (Claude Opus 5.5) | *"Làm hết tất cả những gì có trong giai đoạn 2-3 của Kiên đi!"* (phần Q5) | AI tải bảng vùng và nhóm thu nhập của World Bank qua API công khai (CC BY 4.0) thành `data/raw/country_region.csv`, rồi viết **toàn bộ code và phần mô tả phương pháp** của Q5 trong `notebooks/02_analysis.ipynb`: ghép bảng và báo 11 tên nước không khớp (D1), ma trận thiếu HDI theo năm (D2), cờ thiếu và Bias% (D3), phân tầng theo tuổi, giới, giai đoạn, khu vực (D4), kiểm định Mann-Whitney U, Kolmogorov-Smirnov và cluster bootstrap 1,000 lần (D5), 4 phép kiểm tra độ vững (D6), cùng 4 biểu đồ. AI chạy lại notebook trong môi trường conda để kiểm chứng số liệu; các cell của TV1, TV2 giữ nguyên. AI **không viết** phần kết quả và thảo luận; ô đó để trống cho em tự viết. |
| **06** | 23/11 | Claude Code (Claude Opus 5.5) | *"Làm hết tất cả những gì có trong giai đoạn 2-3 của Kiên đi!"* (phần Q6) | AI viết **toàn bộ code và phần mô tả phương pháp** của Q6 trong `notebooks/03_ml_question.ipynb`: dựng mẫu (t−1, t, t+1) bằng merge theo năm, chia train/test theo năm đích, baseline persistence, CV theo thời gian (5 fold trên danh sách năm), tinh chỉnh Ridge và Random Forest với 2 cách đặt biến đích (mức tỷ lệ và mức thay đổi), đánh giá test một lần, phân tích lỗi, permutation importance, cùng 3 biểu đồ. Việc thêm cách "dự báo mức thay đổi" là đề xuất của AI sau khi thử trên CV của tập train. AI **không viết** phần trả lời và thảo luận kết quả; ô đó để trống cho em tự viết. AI soạn kèm file ghi chú giải thích code và câu tự kiểm tra (không đưa vào repo) để em ôn vấn đáp. |
| **07** | 25/11 | Claude Code (Claude Opus 5.5) | *"Còn phần việc nào nữa vậy? Nếu đã xong thì rà soát lại xem đã làm đúng và đủ hết chưa! Nếu thỏa thì viết file report riêng cho tôi để tôi đọc!"* | AI đối chiếu Q5, Q6 với yêu cầu đề (D1–D6, 6 yêu cầu ML, mục 3.4–3.5), chạy thử bản ghép với nhánh của Huy (3 notebook chạy không lỗi), liệt kê các việc còn thiếu và soạn `Docs/report03.md`. Theo yêu cầu của em, AI cũng đổi tên nhánh thành `feat/kien/q5-q6` theo quy tắc đặt tên của nhóm và bỏ dòng `Co-Authored-By` trong các commit của nhánh. Em dùng danh sách việc còn thiếu để tự viết phần thảo luận và phản tư. |
| **08** | 27/11 | Claude Code (Claude Opus 5.5) | *"Từ KIÊN_Q5_Q6_REVIEW_GUIDE.md hãy làm lại phần của tui đi!"* | AI sắp lại markdown và thứ tự cell của Q5, Q6 theo khung 4 bước của Q1–Q2 (tiêu đề câu hỏi, Tiền xử lý, Phân tích, Trực quan hóa, Thảo luận): tách code vẽ hình khỏi code tính toán, thêm `check_row_count` cho bước lọc 10 năm có HDI, chuyển `%matplotlib inline` lên ô import, đổi các câu dùng "em" sang văn phong khách quan. AI chạy lại 2 notebook và kiểm tra số liệu không đổi. Mục 4 (thảo luận a–d) chỉ có khung, em tự viết nội dung. |


---
*Bảng nhật ký này được các thành viên cập nhật liên tục và độc lập trong suốt quá trình làm đồ án.*
