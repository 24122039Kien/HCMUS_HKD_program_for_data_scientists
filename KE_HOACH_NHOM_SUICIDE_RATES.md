# KẾ HOẠCH CHI TIẾT ĐỒ ÁN CUỐI KỲ (CSC17104 - LẬP TRÌNH CHO KHOA HỌC DỮ LIỆU)
## ĐỀ TÀI: PHÂN TÍCH VÀ DỰ BÁO TỶ LỆ TỰ TỬ TOÀN CẦU (SUICIDE RATES OVERVIEW 1985–2016)
**Khoa Công nghệ Thông tin – Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM (FIT-HCMUS)**  
**Bộ dữ liệu:** Suicide Rates Overview 1985 to 2016 (Kaggle / WHO, World Bank, UNDP) — 27,820 dòng, 12 cột  
**Quy mô nhóm:** 3 thành viên (TV1, TV2, TV3) | **Thời gian thực hiện:** 03/11/2026 – 29/11/2026 (Khóa bản nộp: 27/11/2026)

---

## I. TỔNG QUAN TIẾN ĐỘ 4 GIAI ĐOẠN (MASTER ROADMAP)

Kế hoạch được thiết kế bám sát 100% tài liệu yêu cầu **`CSC17104_2026_Final_Project.pdf`**, trải dài qua 4 giai đoạn chuẩn của chu trình Khoa học Dữ liệu (Data Science Workflow) nhằm đảm bảo cân bằng tải và hoàn thành trước thời hạn nộp 2 ngày:

```
[GIAI ĐOẠN 1: 03/11 – 09/11 | THU THẬP & KHÁM PHÁ DỮ LIỆU (EDA)]
  ├── Thiết lập Git, Conda, cấu trúc repo, file .gitignore, LLM_USAGE.md
  ├── Mục 3.1: Hoàn thành 5 câu hỏi Data Collection & Khai báo công trình tham khảo
  ├── Phân chia 12 cột dữ liệu cho 3 thành viên kiểm tra chuyên sâu
  └── Chốt danh sách 6 câu hỏi định hướng (5 Non-ML, 1 ML) & Tóm tắt EDA (3-5 Key Obs, Data Issues, Preprocessing Plan)
  ▼
[GIAI ĐOẠN 2: 06/11 – 14/11 | ĐẶC TẢ CÂU HỎI, TIỀN XỬ LÝ & PHÂN TÍCH BƯỚC ĐẦU]
  ├── Mục 3.3: Viết chi tiết đặc tả 6 câu hỏi (Motivation, Target User, Decision)
  ├── Mục 3.4: Tiền xử lý dữ liệu cho từng câu hỏi (BẮT BUỘC in và báo cáo số dòng trước/sau mỗi bước)
  ├── Dựng khung mô-đun dùng chung trong src/ (utils.py, visualization.py)
  └── Hoàn thành bản nháp phân tích Q1–Q5 & Dựng sườn Pipeline ML + Trivial Baseline Q6 trên tập Train
  ▼
[GIAI ĐOẠN 3: 15/11 – 21/11 | HOÀN THIỆN PHÂN TÍCH, TỐI ƯU HỌC MÁY & ĐÚC KẾT INSIGHT]
  ├── Mục 3.4: Hoàn thiện trực quan hóa (≥ 2 plots chuẩn học thuật/câu hỏi; đủ title, axes, units, legend, n)
  ├── Trả lời định lượng bằng con số cho từng câu hỏi, thảo luận ý nghĩa thực tiễn, điểm bất ngờ & giới hạn
  ├── Mục 3.4 (ML): CV Hyperparameter Tuning trên Train, đánh giá Test set ĐÚNG 1 LẦN, Error Analysis, XAI
  └── Mục 3.5: Viết Summary (3–5 Key Findings, Limitations, Future Work) & Phản tư cá nhân (Individual Reflection)
  ▼
[GIAI ĐOẠN 4: 22/11 – 27/11 | ĐÓNG GÓI TÁI LẬP, THIẾT KẾ SLIDE, TẬP BẢO VỆ & KHÓA NỘP]
  ├── Rà soát tính tái lập (Reproducibility): Chạy lại toàn bộ notebook trên môi trường Conda mới sạch
  ├── Hoàn thiện README.md chuẩn rubric, đồng bộ commit Git cá nhân, chuẩn hóa LLM_USAGE.md
  ├── Thiết kế slide báo cáo (slides.pdf - chuẩn 15 phút thuyết trình Data Storytelling, không paste code)
  ├── Tổ chức buổi Vấn đáp thử nội bộ (Mock Defense: 15 phút nói + 10 phút hỏi đáp chéo)
  ├── 27/11: Khóa bản nộp chính thức (Buffer dự phòng 28/11; Nộp bài 29/11)
```

---

## II. MA TRẬN PHÂN CÔNG VAI TRÒ VÀ TRÁCH NHIỆM THÀNH VIÊN

Nhằm đảm bảo điểm số cá nhân công bằng và đúng rubric (từng thành viên tự commit, nắm vững toàn bộ bài thi), vai trò được phân định rõ ràng xuyên suốt đồ án:

| Thành viên | Trách nhiệm cốt lõi | Phụ trách câu hỏi | Đầu mối tài liệu / Mã nguồn |
| :--- | :--- | :---: | :--- |
| **TV1** *(Trưởng nhóm)* | **Kiến trúc dữ liệu, Không gian & Thời gian**<br>• Quản trị Git Repo, cấu trúc thư mục, `environment.yml`.<br>• Soạn thảo Mục 3.1 (Data Collection) & Tổng hợp notebook EDA 01.<br>• Phân tích khóa định danh `country-year`, tính toàn vẹn dữ liệu chuỗi thời gian.<br>• Khởi tạo thư mục `src/utils.py` chứa các hàm xử lý dữ liệu dùng chung.<br>• Rà soát chéo phần việc của TV2. | **Q1** *(Non-ML)*<br>**Q2** *(Non-ML)* | • `notebooks/01_collection_exploration.ipynb`<br>• `notebooks/02_analysis_q1_q2.ipynb`<br>• `README.md` (Hướng dẫn cài đặt & tái lập)<br>• `src/utils.py` |
| **TV2** | **Kinh tế - Xã hội, Chuẩn hóa Dân số & Trực quan hóa**<br>• Phân tích chuyên sâu nhóm cột định lượng: Dân số, Số ca, Tỷ lệ thô, GDP.<br>• Thiết lập module `src/visualization.py` chuẩn hóa style đồ thị toàn nhóm.<br>• Triển khai kỹ thuật Chuẩn hóa trực tiếp theo tuổi (Direct Age Standardization).<br>• Chủ trì tổng hợp Mục 3.5 (Key Findings, Limitations, Future Work).<br>• Phụ trách biên tập và xuất file slide thuyết trình `slides.pdf`.<br>• Rà soát chéo phần việc của TV3. | **Q3** *(Non-ML)*<br>**Q4** *(Non-ML)* | • `notebooks/02_analysis_q3_q4.ipynb`<br>• `src/visualization.py`<br>• `slides.pdf`<br>• Đóng góp Mục 3.5 trong báo cáo |
| **TV3** | **Nhân khẩu học, Xử lý Khuyết thiếu & Học máy (ML)**<br>• Phân tích chuyên sâu nhóm cột định danh (Sex, Age, Generation) và biến thiếu `HDI for year`.<br>• Khảo sát cơ chế khuyết thiếu (Missing mechanism) và bóp méo ước lượng.<br>• Thiết kế và tối ưu toàn bộ Machine Learning Pipeline cho Q6 (chuẩn rubric mục 4.3 đề thi).<br>• Quản lý file nhật ký AI `LLM_USAGE.md` & Điều phối buổi vấn đáp thử (Mock Q&A).<br>• Rà soát chéo phần việc của TV1. | **Q5** *(Non-ML)*<br>**Q6** *(Machine Learning)* | • `notebooks/02_analysis_q5.ipynb`<br>• `notebooks/03_ml_question.ipynb`<br>• `LLM_USAGE.md`<br>• Kịch bản câu hỏi phản biện nội bộ |

---

## III. CHI TIẾT 12 TRƯỜNG DỮ LIỆU & PHÂN BỔ KHÁM PHÁ (MỤC 3.2 EDA)

Bộ dữ liệu gồm **27,820 dòng và 12 cột** (ghi nhận từ 1985 đến 2016 trên 101 quốc gia). Phân chia 12 cột cho từng thành viên kiểm tra chuyên sâu, tránh làm trùng lặp:

```
                                      BỘ DỮ LIỆU: SUICIDE RATES (12 CỘT)
                                                      │
         ┌────────────────────────────────────────────┼────────────────────────────────────────────┐
         ▼                                            ▼                                            ▼
   [TV1: ĐỊNH DANH & THỜI GIAN]                 [TV2: SỐ LIỆU & KINH TẾ]                     [TV3: NHÂN KHẨU & PHÁT TRIỂN]
   • country (Chuẩn hóa tên quốc gia)           • suicides_no (Số ca tự tử ghi nhận)         • sex (male, female)
   • year (1985–2016, kiểm tra tính liên tục)   • population (Dân số của phân nhóm)          • age (6 nhóm tuổi cố định)
   • country-year (Khóa ghép kiểm tra)          • suicides/100k pop (Tỷ lệ trên 100k dân)    • generation (6 thế hệ nhân khẩu)
                                                •  gdp_for_year ($)  (GDP quốc gia/năm)      • HDI for year (Chỉ số phát triển
                                                • gdp_per_capita ($) (GDP bình quân đầu)       con người - thiếu ~69%)
```

### Nhiệm vụ kiểm tra cụ thể của từng thành viên:
1. **TV1 (`country`, `year`, `country-year`):**
   - Xác định rõ ngữ nghĩa 1 dòng: *Là số liệu thống kê tự tử của một nhóm tuổi–giới tính cụ thể tại một quốc gia trong một năm xác định*.
   - Kiểm tra tính toàn vẹn của khóa chính tổng hợp: `(country, year, sex, age)`. Đảm bảo không có dòng trùng lặp hoàn toàn (`drop_duplicates` nếu có).
   - Kiểm tra tính đồng nhất giữa cột khóa ghép `country-year` với hai cột thành phần `country` và `year`.
   - Lập bảng độ phủ thời gian: Đếm số năm có dữ liệu của từng quốc gia. Phát hiện các quốc gia chỉ xuất hiện 1–2 năm hoặc đứt quãng; phát hiện năm 2016 bị thiếu dữ liệu trầm trọng (chỉ có rất ít quốc gia nộp báo cáo) để đưa ra khuyến nghị lọc cửa sổ thời gian.
2. **TV2 (`suicides_no`, `population`, `suicides/100k pop`, ` gdp_for_year ($) `, `gdp_per_capita ($)`):**
   - Xử lý lỗi định dạng tên cột: Tên cột GDP gốc trong CSV có khoảng trắng ở đầu và cuối: `' gdp_for_year ($) '` $\rightarrow$ Đổi tên chuẩn hóa thành `gdp_for_year`.
   - Ép kiểu dữ liệu: Cột `gdp_for_year` chứa dấu phẩy phân cách hàng nghìn (kiểu chuỗi) $\rightarrow$ Ép kiểu về `int64`/`float64`.
   - Sanity check & Outliers: Kiểm tra số ca âm (`suicides_no < 0`), dân số bằng 0 (`population == 0`). Kiểm tra sai số làm tròn của `suicides/100k pop` so với công thức chuẩn $100{,}000 \times \frac{\text{suicides\_no}}{\text{population}}$.
   - Phân tích phân phối (skewness), tính chất ngoại lệ (outlier do quốc gia dân số siêu nhỏ như Grenada, San Marino hay siêu lớn như Mỹ, Nga).
   - Kiểm tra tính nhất quán của GDP: Trong cùng một `country-year`, giá trị GDP của các dòng con (tuổi–giới) phải bằng nhau trước khi thực hiện phép gộp.
3. **TV3 (`sex`, `age`, `generation`, `HDI for year`):**
   - Khảo sát cột phân loại `sex` (2 nhãn) và `age` (6 nhóm tuổi: `5-14`, `15-24`, `25-34`, `35-54`, `55-74`, `75+`). Kiểm tra xem mỗi quốc gia trong 1 năm có đúng $2 \times 6 = 12$ dòng hay bị thiếu nhóm tuổi/giới nào.
   - Khảo sát biến `generation`: Phân tích mối liên hệ toán học giữa `age`, `year` và `generation` để xem đây có phải biến dư thừa (redundant) hay không.
   - Khảo sát sâu biến khuyết thiếu `HDI for year`: Thống kê số lượng và tỷ lệ missing (thiếu ~69.6%). Xác định cơ chế thiếu: UNDP chỉ đo lường HDI vào các năm mốc (1990, 1995, 2000, 2005) và liên tục từ 2010 trở đi. Đưa ra đề xuất phương án xử lý cho Q5 và Q6.
   - Thống kê số lượng cặp năm liên tiếp ($t$ và $t+1$) đủ điều kiện để tạo tập dữ liệu cho bài toán Machine Learning (Q6).

---

## IV. BẢN ĐẶC TẢ CHI TIẾT 6 CÂU HỎI NGHIÊN CỨU (MỤC 3.3 & 3.4)

Mỗi câu hỏi được thiết kế thỏa mãn tuyệt đối các tiêu chí chiều sâu trong đề cương:
- **5 câu Non-ML:** Mỗi câu thỏa mãn ít nhất 2 tiêu chí, tổng thể phủ trọn vẹn **D1, D2, D3, D4, D5, D6** (tất cả 6/6 tiêu chí).
- **1 câu ML (Q6):** Thỏa mãn đầy đủ 6 yêu cầu khắt khe (No leakage, Time-based split, Pipeline, Baseline + 2 Models, Error Analysis, XAI).

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                              MA TRẬN 6 CÂU HỎI NGHIÊN CỨU                                              │
├──────┬─────────┬───────┬──────────────────────────────────────────────────────────┬────────────────────────────────────┤
│ Mã   │ Loại    │ Chủ sở│ Tóm tắt chủ đề câu hỏi                                   │ Tiêu chí chiều sâu thỏa mãn        │
├──────┼─────────┼───────┼──────────────────────────────────────────────────────────┼────────────────────────────────────┤
│ **Q1**│ Non-ML  │  TV1  │ Xu hướng toàn cầu: Mẫu cố định (Cohort) vs Mẫu đầy đủ     │ **D2, D3, D6**                     │
│ **Q2**│ Non-ML  │  TV1  │ Chênh lệch tỷ lệ Nam - Nữ theo độ tuổi và Bootstrap CI   │ **D3, D4, D5**                     │
│ **Q3**│ Non-ML  │  TV2  │ Biến động GDP bình quân đầu người và Tỷ lệ tử vong       │ **D2, D3, D4, D6**                 │
│ **Q4**│ Non-ML  │  TV2  │ Tác động của già hóa dân số: Tỷ lệ thô vs Chuẩn hóa tuổi │ **D2, D3, D4, D6**                 │
│ **Q5**│ Non-ML  │  TV3  │ Cơ chế thiếu dữ liệu HDI và Sai lệch ước lượng theo tuổi │ **D1, D2, D3, D4, D5, D6**         │
│ **Q6**│ **ML**  │  TV3  │ Hệ thống cảnh báo sớm: Dự báo tỷ lệ năm t+1 không rò rỉ  │ **ML Criteria 1–6 (Đạt chuẩn 100%)**│
└──────┴─────────┴───────┴──────────────────────────────────────────────────────────┴────────────────────────────────────┘
```

### 1. Câu hỏi 1 (TV1): Xu hướng tỷ lệ tử vong do tự tử toàn cầu qua các thập kỷ
- **Nội dung:** *Xu hướng tỷ lệ tử vong do tự tử toàn cầu thay đổi như thế nào từ năm 1990 đến 2015 khi theo dõi trên cùng một tập hợp quốc gia có dữ liệu liên tục (Fixed Balanced Cohort) so với việc tính toán trên tất cả các quốc gia có dữ liệu tại từng năm?*
- **Động cơ & Quyết định:** Giúp các nhà dịch tễ học và WHO nhận diện **thiên lệch chọn mẫu (Selection Bias)**. Nếu chỉ lấy trung bình các nước nộp báo cáo mỗi năm, xu hướng giảm có thể là "ảo" do các nước mới gia nhập có tỷ lệ thấp hơn. Giúp quyết định cách xây dựng chỉ số giám sát toàn cầu đáng tin cậy.
- **Tiêu chí chiều sâu:**
  - **D2 (Reshaping & time):** Xây dựng bảng chuỗi thời gian (pivot table), tính toán chỉ số biến động qua từng năm (period-over-period) và rolling average 3 năm.
  - **D3 (Derived variables):** Tính tỷ lệ tổng hợp đúng đắn: $100{,}000 \times \frac{\sum \text{suicides}}{\sum \text{population}}$ thay vì lấy trung bình cộng của các cột tỷ lệ có sẵn.
  - **D6 (Robustness check):** Kiểm tra tính vững bằng cách thay đổi ngưỡng định nghĩa Cohort (quốc gia có đủ dữ liệu 100% các năm vs quốc gia có dữ liệu $\ge 90\%$ số năm; thay đổi cửa sổ 1990–2015 sang 1995–2014).
- **Yêu cầu trực quan hóa:** 
  - Biểu đồ 1: Line plot so sánh chuỗi tỷ lệ toàn cầu giữa "Fixed Cohort" và "All Available Countries" (có vùng bóng biểu diễn biến động).
  - Biểu đồ 2: Heatmap hoặc Bar chart thể hiện số lượng quốc gia báo cáo theo từng năm và mức độ chênh lệch phần trăm giữa 2 phương pháp.

### 2. Câu hỏi 2 (TV1): Chênh lệch tỷ lệ tử vong giữa Nam và Nữ theo độ tuổi
- **Nội dung:** *Chênh lệch tỷ lệ tử vong do tự tử giữa nam và nữ biến động như thế nào qua 6 nhóm tuổi trong cùng một quốc gia và năm, và khoảng tin cậy của mức chênh lệch này là bao nhiêu khi xét trên phạm vi toàn cầu?*
- **Động cơ & Quyết định:** Hỗ trợ các cơ quan y tế công cộng xác định nhóm dân số có rủi ro cao nhất cần ưu tiên can thiệp tâm lý (đặc biệt kiểm chứng giả thuyết "nam giới lớn tuổi có mức chênh lệch áp đảo"). Giúp phân bổ ngân sách phòng chống tự tử trúng đích theo nhóm tuổi và giới tính.
- **Tiêu chí chiều sâu:**
  - **D3 (Derived variables):** Tạo biến chênh lệch tuyệt đối $\text{Rate\_Diff} = \text{Rate}_{\text{Male}} - \text{Rate}_{\text{Female}}$ và tỷ số giới tính $\text{Sex\_Ratio} = \frac{\text{Rate}_{\text{Male}}}{\text{Rate}_{\text{Female}}}$.
  - **D4 (Controlling for a confounder):** Ghép cặp hoàn hảo theo từng đơn vị `(country, year, age)` để loại bỏ triệt để yếu tố gây nhiễu về quốc gia và thời gian trước khi so sánh giới tính.
  - **D5 (Quantifying uncertainty):** Áp dụng kỹ thuật **Non-parametric Bootstrap** (1,000 lần lặp, lấy mẫu lại theo cấp quốc gia để giữ nguyên cấu trúc cụm) để tính **Khoảng tin cậy 95% (95% CI)** cho mức chênh lệch trung bình ở từng nhóm tuổi.
- **Yêu cầu trực quan hóa:**
  - Biểu đồ 1: Forest plot hoặc Point plot hiển thị chênh lệch trung bình kèm thanh sai số 95% Bootstrap CI cho 6 nhóm tuổi.
  - Biểu đồ 2: Boxplot hoặc Violin plot thể hiện phân phối tỷ số Nam/Nữ trên các khu vực địa lý / nhóm quốc gia.

### 3. Câu hỏi 3 (TV2): Mối liên hệ giữa biến động GDP bình quân đầu người và tỷ lệ tự tử
- **Nội dung:** *Trong nội bộ cùng một quốc gia, mức thay đổi phần trăm của GDP bình quân đầu người qua từng năm có mối liên hệ cùng chiều hay ngược chiều với mức thay đổi của tỷ lệ tự tử, và mối liên hệ này có thay đổi theo mức thu nhập quốc gia không?*
- **Động cơ & Quyết định:** Kiểm chứng lý thuyết kinh tế - xã hội về tác động của suy thoái kinh tế đối với sức khỏe tâm thần. Cung cấp bằng chứng thực nghiệm cho các nhà hoạch định chính sách an sinh xã hội: Liệu tăng trưởng kinh tế có tự động làm giảm tự tử, hay các đợt khủng hoảng ngắn hạn tạo ra cú sốc nghiêm trọng hơn?
- **Tiêu chí chiều sâu:**
  - **D2 (Reshaping & time):** Gộp dữ liệu về cấp `(country, year)`, tạo biến trễ (lag 1 năm), tính tốc độ tăng trưởng liên năm: $\% \Delta \text{GDP} = \frac{\text{GDP}_t - \text{GDP}_{t-1}}{\text{GDP}_{t-1}} \times 100$ và $\Delta \text{Suicide\_Rate} = \text{Rate}_t - \text{Rate}_{t-1}$.
  - **D3 (Derived variables):** Biến phân loại nhóm kinh tế (Quốc gia thu nhập cao, trung bình, thấp theo phân vị GDP) và biến tương đối hóa tốc độ biến thiên.
  - **D4 (Controlling for a confounder):** Sử dụng phương pháp First-difference (lấy sai phân bậc nhất trong nội bộ từng quốc gia) nhằm triệt tiêu hoàn toàn các biến gây nhiễu cố định theo thời gian của từng nước (văn hóa, tôn giáo, đặc điểm địa lý).
  - **D6 (Robustness check):** Kiểm tra tính vững bằng cách thử nghiệm độ trễ 2 năm (lag 2), loại bỏ các năm có biến động kinh tế cực đoan ($> 20\%$) và kiểm tra riêng trên nhóm các nước có GDP cao.
- **Yêu cầu trực quan hóa:**
  - Biểu đồ 1: Scatter plot có đường hồi quy biểu diễn $\% \Delta \text{GDP}$ và $\Delta \text{Suicide\_Rate}$ phân tầng theo 3 nhóm mức thu nhập.
  - Biểu đồ 2: Biểu đồ đường kép (Dual-axis time series) thể hiện diễn biến GDP và tỷ lệ tự tử của một số quốc gia điển hình trải qua khủng hoảng kinh tế (ví dụ: Khủng hoảng tài chính châu Á 1997 hoặc Khủng hoảng toàn cầu 2008).

### 4. Câu hỏi 4 (TV2): Tác động của già hóa dân số – Tỷ lệ thô vs Tỷ lệ chuẩn hóa theo tuổi
- **Nội dung:** *Mức độ thay đổi của tỷ lệ tử vong do tự tử giữa hai giai đoạn (1995–2000 so với 2010–2015) trên cùng một tập quốc gia bị chi phối bao nhiêu phần trăm bởi sự già hóa dân số (thay đổi cơ cấu tuổi - giới tính)?*
- **Động cơ & Quyết định:** Giúp các nhà dịch tễ học và quản lý y tế cộng đồng đánh giá chính xác hiệu quả can thiệp y tế: Tránh kết luận sai lầm rằng tình hình đang xấu đi trong khi thực tế chỉ do dân số đang già đi (nhóm tuổi cao vốn có tỷ lệ tử vong nền cao hơn).
- **Tiêu chí chiều sâu:**
  - **D2 (Reshaping & time):** Tổng hợp dữ liệu thành 2 thời kỳ 5 năm (1995–2000 vs 2010–2015), pivot bảng dữ liệu để so sánh period-over-period.
  - **D3 (Derived variables):** Xây dựng công thức tính **Tỷ lệ Chuẩn hóa trực tiếp theo tuổi (Direct Age-Standardized Rate - ASR)**:
    $$\text{ASR} = \frac{\sum_{i} (\text{Rate}_i \times w_i)}{\sum_i w_i}$$
    với $w_i$ là trọng số dân số chuẩn tham chiếu của nhóm tuổi $i$.
  - **D4 (Controlling for a confounder):** Khống chế triệt để biến gây nhiễu là **sự thay đổi cơ cấu độ tuổi dân số** giữa hai thời kỳ.
  - **D6 (Robustness check):** Kiểm tra tính vững bằng cách so sánh kết quả khi dùng bộ trọng số chuẩn WHO Standard Population với bộ trọng số tính từ dân số trung bình toàn cầu trong chính dataset.
- **Yêu cầu trực quan hóa:**
  - Biểu đồ 1: Dumbbell plot (biểu đồ quả tạ) hoặc Slope chart so sánh mức thay đổi của Tỷ lệ thô (Crude Rate) vs Tỷ lệ chuẩn hóa (ASR) ở top 15 quốc gia già hóa nhanh nhất.
  - Biểu đồ 2: Stacked bar chart thể hiện sự dịch chuyển tỷ trọng các nhóm tuổi trong dân số giữa hai giai đoạn.

### 5. Câu hỏi 5 (TV3): Khảo sát dữ liệu thiếu của HDI và sai lệch ước lượng theo nhóm tuổi
- **Nội dung:** *Chỉ số phát triển con người (HDI for year) bị thiếu như thế nào theo quốc gia và giai đoạn thời gian, và việc chỉ giữ lại các dòng có đầy đủ dữ liệu HDI (Complete-case Analysis) có làm sai lệch ước lượng tỷ lệ tử vong theo độ tuổi hay không, đặc biệt khi so sánh giữa các khu vực địa lý?*
- **Động cơ & Quyết định:** Giúp các nhà nghiên cứu dữ liệu đánh giá cơ chế Missing Data (MCAR vs MAR/MNAR) trước khi quyết định đưa biến HDI vào mô hình kinh tế lượng. Quyết định xem có nên impute HDI hay chấp nhận loại bỏ mẫu, nhận diện nguy cơ kết luận sai do chỉ giữ lại các nước phát triển.
- **Tiêu chí chiều sâu:**
  - **D1 (Combining data):** Ghép bảng phân loại khu vực địa lý/châu lục cho các quốc gia từ nguồn ngoài (file `country_region.csv` chuẩn World Bank / UN M49) vào dataset chính theo khóa `country`. Báo cáo số dòng trước/sau khi ghép và các quốc gia không khớp (unmatched keys) — ví dụ: "Republic of Korea" vs "South Korea" cần chuẩn hóa tên.
  - **D2 (Reshaping & time):** Khảo sát ma trận thiếu theo trục thời gian (1985–2016), phân chia các giai đoạn thu thập HDI của Liên Hợp Quốc (trước 2010 đo định kỳ 5 năm, sau 2010 đo hàng năm).
  - **D3 (Derived variables):** Tạo biến cờ thiếu dữ liệu `is_missing_hdi`, tính tỷ lệ sai lệch tương đối (Relative Bias %):
    $$\text{Bias}\% = \frac{\text{Rate}_{\text{Complete}} - \text{Rate}_{\text{All}}}{\text{Rate}_{\text{All}}} \times 100$$
  - **D4 (Controlling for a confounder):** Phân tích sai lệch phân tầng độc lập theo 6 nhóm tuổi, từng khối thời gian và từng **khu vực địa lý** (châu Á, châu Âu, châu Mỹ, châu Phi...).
  - **D5 (Quantifying uncertainty):** Thực hiện kiểm định thống kê hai mẫu (Two-sample Kolmogorov-Smirnov test hoặc Mann-Whitney U test) để kiểm tra xem phân phối tỷ lệ giữa tập có HDI và tập thiếu HDI có khác biệt có ý nghĩa thống kê hay không ($p$-value).
  - **D6 (Robustness check):** Kiểm tra độ nhạy trên các quốc gia có độ bao phủ HDI cao ($> 80\%$) so với các quốc gia có độ bao phủ thấp ($< 30\%$).
- **Yêu cầu trực quan hóa:**
  - Biểu đồ 1: Missingness matrix / Heatmap biểu diễn tỷ lệ có dữ liệu HDI của các quốc gia theo từng năm từ 1985 đến 2016, tô màu theo khu vực địa lý.
  - Biểu đồ 2: Bar chart nhóm so sánh tỷ lệ tự tử trung bình của 6 nhóm tuổi giữa "Tập đầy đủ toàn bộ" và "Tập lọc chỉ giữ các dòng có HDI", kèm $p$-value kiểm định.
  - Biểu đồ 3: (Bổ sung từ D1) Bar chart hoặc Choropleth map thể hiện tỷ lệ thiếu HDI theo từng khu vực địa lý.

### 6. Câu hỏi 6 (TV3 - Machine Learning): Dự báo tỷ lệ tử vong năm kế tiếp (t+1)
- **Nội dung:** *Với dữ liệu thống kê sẵn có đến hết năm $t$, một hệ thống giám sát y tế công cộng có thể dự báo tỷ lệ tử vong do tự tử ở cấp độ nhóm (quốc gia–tuổi–giới tính) cho năm kế tiếp ($t+1$) với độ chính xác vượt trội hơn bao nhiêu so với mô hình cơ sở giữ nguyên tỷ lệ năm gần nhất?*
- **Bảo đảm 6 tiêu chuẩn khắt khe của Đề bài môn học:**
  1. **Người dùng & Chống rò rỉ dữ liệu (No Data Leakage):**
     - *Người dùng mục tiêu:* Ban giám sát dịch tễ của WHO / Bộ Y tế các quốc gia cần tín hiệu cảnh báo sớm trước 1 năm để kích hoạt chiến dịch can thiệp tâm lý cộng đồng.
     - *Quy tắc chống rò rỉ tuyệt đối:* Biến đích (Target) là `suicides/100k pop` tại năm $t+1$. **Loại bỏ 100% các cột thuộc về năm $t+1$** (gồm: `suicides_no`, `population`, `gdp_for_year`, `gdp_per_capita`, `HDI for year` của năm $t+1$).
     - *Không gian đặc trưng (Feature space):* Chỉ dùng thông tin ghi nhận tại năm $t$: `country`, `sex`, `age`, `generation`, `suicides/100k pop` năm $t$, biến trễ năm $t-1$, tốc độ thay đổi liên năm $\Delta \text{Rate}_{t, t-1}$, `population` năm $t$, `gdp_per_capita` năm $t$.
  2. **Chiến lược phân chia tập dữ liệu (Time-based Split):**
     - Dữ liệu là chuỗi thời gian, tuyệt đối không dùng chia ngẫu nhiên.
     - **Tập Train:** Dữ liệu có năm đích $t+1$ từ **1990 đến 2010** (~80% thời gian).
     - **Tập Test:** Dữ liệu có năm đích $t+1$ từ **2011 đến 2015** (~20% thời gian). Giữ nguyên toàn bộ các dòng của cùng một năm trong cùng một tập.
  3. **Mô hình cơ sở & Pipeline:**
     - **Trivial Baseline:** *Naive Persistence Model* — Dự đoán tỷ lệ năm $t+1$ bằng chính tỷ lệ ghi nhận tại năm $t$: $\hat{y}_{t+1} = y_t$.
     - **2 Mô hình Học máy đối chứng:**
       - Model 1: **Ridge Regression** (Linear model có điều chuẩn $L_2$).
       - Model 2: **Random Forest Regressor** (Non-linear ensemble tree model).
     - **Scikit-learn Pipeline:** Toàn bộ bước tiền xử lý (OneHotEncoder cho biến danh mục `sex`, `age`, `country`; StandardScaler cho biến số; SimpleImputer cho biến khuyết) phải được bao gói hoàn toàn bên trong Pipeline để ngăn rò rỉ dữ liệu từ tập thẩm định sang tập huấn luyện.
  4. **Cross-Validation & Thước đo đánh giá (Evaluation Metric):**
     - Tinh chỉnh siêu tham số (Hyperparameter tuning) bằng **TimeSeriesSplit** (5 folds) hoặc **GroupKFold (theo năm)** **CHỈ TRÊN TẬP TRAIN**.
     - Đánh giá trên tập Test **ĐÚNG 1 LẦN DUY NHẤT** sau khi đã chốt mô hình và siêu tham số tốt nhất.
     - *Biện luận thước đo:* Sử dụng **MAE (Mean Absolute Error)** làm metric chính (đơn vị: số ca/100,000 dân, rất trực quan và có ý nghĩa thực tiễn với chuyên gia y tế), đi kèm **RMSE** để quan sát mức độ phạt các sai số cực đoan.
  5. **Phân tích lỗi mô hình (Error Analysis):**
     - Đánh giá phân phối sai số tuyệt đối ($|y - \hat{y}|$).
     - Phân tích chi tiết mô hình dự báo kém ở những phân nhóm nào: So sánh MAE theo 6 nhóm tuổi, theo giới tính, và theo mức tỷ lệ tử vong nền (nhóm tỷ lệ cao $> 30$ vs nhóm tỷ lệ thấp $< 5$). Trích xuất 5 dòng có sai số lớn nhất để giải thích nguyên nhân dịch tễ học thực tế.
  6. **Giải thích mô hình (XAI) & Trả lời câu hỏi gốc:**
     - Sử dụng **Permutation Feature Importance** trên tập test để xác định đâu là các yếu tố có sức nặng dự báo lớn nhất.
     - Trả lời trực tiếp câu hỏi nghiên cứu bằng con số cụ thể: *Mô hình Random Forest cải thiện được bao nhiêu phần trăm MAE so với Trivial Baseline? Mô hình có đủ độ tin cậy để triển khai thực tế không?*
- **Yêu cầu trực quan hóa:**
  - Biểu đồ 1: Actual vs Predicted Scatter plot trên tập Test cho Baseline và Random Forest (kèm đường phân giác $y=x$).
  - Biểu đồ 2: Bar plot thể hiện Permutation Feature Importance của top các đặc trưng quan trọng nhất.
  - Biểu đồ 3: Error breakdown bar chart so sánh MAE giữa các nhóm tuổi và giới tính.

---

## V. PHÂN CHIA CÔNG VIỆC CHI TIẾT THEO TỪNG GIAI ĐOẠN & LỊCH TRÌNH THỰC THI

Tiến độ thực tế diễn ra từ ngày **03/11 đến 29/11/2026** (Khóa bản nộp ngày 27/11, dư 2 ngày dự phòng sự cố). Khối lượng công việc trong từng giai đoạn được phân bổ theo bảng trách nhiệm cụ thể, đi kèm sản phẩm bàn giao (Deliverables), cơ chế rà soát chéo và lịch trình hành động từng ngày:

```
GIAI ĐOẠN 1 (03–09/11): Setup hạ tầng, Khám phá dữ liệu (EDA) & Chốt đề cương 6 câu hỏi
GIAI ĐOẠN 2 (10–16/11): Đặc tả câu hỏi, Tiền xử lý dữ liệu & Phân tích bước đầu + Baseline ML
GIAI ĐOẠN 3 (17–23/11): Hoàn tất phân tích chuyên sâu, CV Tuning ML, 12 biểu đồ & Đúc kết Insight
GIAI ĐOẠN 4 (24–29/11): Kiểm tra tái lập, Thiết kế slide, Tập bảo vệ nội bộ & Khóa nộp bài
```

---

### GIAI ĐOẠN 1: THU THẬP & KHÁM PHÁ DỮ LIỆU (EDA) (03/11 – 09/11)

#### 1. Bảng phân chia công việc Giai đoạn 1:
| Thành viên | Nhiệm vụ cụ thể trong Giai đoạn 1 | Sản phẩm bàn giao (Deliverables) | Người rà soát chéo |
| :--- | :--- | :--- | :---: |
| **TV1** *(Trưởng nhóm)* | • Khởi tạo Git Repo, thiết lập cấu trúc thư mục chuẩn, `.gitignore` và `environment.yml` cơ bản.<br>• Viết toàn bộ **Mục 3.1 Data Collection** (Subject, Source URL, License, Collection method, Known biases) và phần khai báo công trình tham khảo (Declare existing work).<br>• Phụ trách **Mục 3.2 Overview**: Số dòng/cột, kiểu dữ liệu, duplicates, định nghĩa 1 dòng dữ liệu.<br>• Khảo sát chuyên sâu cột định danh & chuỗi thời gian (`country`, `year`, `country-year`): Tính duy nhất của khóa tổng hợp, lập bảng độ phủ thời gian, phát hiện năm 2016 thiếu dữ liệu.<br>• Review code và tổng hợp merge vào `notebooks/01_collection_exploration.ipynb`. | • Repo GitHub chuẩn hóa.<br>• File `environment.yml`.<br>• Mục 3.1 hoàn chỉnh 100%.<br>• Đoạn code EDA Overview và độ phủ không gian - thời gian. | **TV2** |
| **TV2** | • Phụ trách khám phá chuyên sâu nhóm cột định lượng & kinh tế: `suicides_no`, `population`, `suicides/100k pop`, ` gdp_for_year ($) `, `gdp_per_capita ($)`.<br>• Xử lý lỗi khoảng trắng tên cột GDP và ép kiểu dữ liệu chuỗi sang số nguyên/thực.<br>• Sanity checks: Kiểm tra ca âm, dân số = 0, phát hiện outliers (quốc gia dân số siêu nhỏ vs siêu lớn), kiểm tra sai số làm tròn của cột tỷ lệ.<br>• Khảo sát hình dạng phân phối (skewness), tính toán ma trận tương quan giữa GDP và tỷ lệ tự tử.<br>• Đề xuất quy tắc làm sạch và chuẩn hóa nhóm biến số cho Giai đoạn 2. | • Đoạn code EDA nhóm cột số (kèm biểu đồ boxplot, histogram phân phối).<br>• Bảng kiểm tra chất lượng biến số và ghi chú xử lý khoảng trắng cột GDP.<br>• Đề xuất quy tắc gộp cấp `country-year`. | **TV3** |
| **TV3** | • Phụ trách khám phá chuyên sâu nhóm cột nhân khẩu học & phát triển: `sex`, `age`, `generation`, `HDI for year`.<br>• Khảo sát cột phân loại `sex` và `age`: Đếm số nhãn, kiểm tra độ cân bằng, xác nhận mỗi quốc gia–năm có đủ 12 phân nhóm hay không.<br>• Khảo sát biến `generation`: Phân tích mối liên hệ logic giữa `age`, `year` và `generation`.<br>• Khảo sát chuyên sâu biến khuyết thiếu `HDI for year`: Thống kê số lượng/tỷ lệ missing (~69.6%), lập bảng/heatmap missing theo chuỗi năm và giai đoạn.<br>• Thống kê số cặp năm liền kề ($t, t+1$) đủ điều kiện dự báo cho bài toán ML (Q6). | • Đoạn code EDA nhóm cột danh mục và nhân khẩu học.<br>• Heatmap / Bảng ma trận dữ liệu thiếu của biến HDI theo năm.<br>• Thống kê số lượng quan sát hợp lệ cho bài toán ML Q6. | **TV1** |
| **Cả nhóm (3 người)** | • Cùng thảo luận và viết phần **Motivation** (Lý do chọn đề tài tỷ lệ tự tử toàn cầu, ý nghĩa nhân văn và tính cấp thiết thực tiễn).<br>• Mở file `LLM_USAGE.md` ghi nhận phiên làm việc đầu tiên với công cụ AI.<br>• Họp nhóm chốt 6 câu hỏi chính thức (5 Non-ML, 1 ML) và xác định người sở hữu từng câu.<br>• Cùng viết phần tổng kết cuối mục 3.2: **3–5 Key observations**, **Serious data quality issues**, và **Preprocessing plan**. | • Mục Motivation thống nhất.<br>• Danh sách 6 câu hỏi chính thức.<br>• File `LLM_USAGE.md` khởi tạo.<br>• Tóm tắt cuối Mục 3.2 hoàn chỉnh. | Cả nhóm |

#### 2. Kế hoạch hành động theo ngày (Day-by-Day):
- **Thứ Hai (03/11):** TV1 setup Git, `.gitignore`, `environment.yml`, tải `master.csv` vào `data/raw/`. Soạn Mục 3.1. Cả nhóm viết Motivation và mở `LLM_USAGE.md`.
- **Thứ Ba – Thứ Tư (04–05/11):** 3 thành viên độc lập chạy code EDA 12 cột theo phân công trên nhánh riêng.
- **Thứ Năm (06/11):** Họp nhóm 45 phút, TV1 merge code vào `01_collection_exploration.ipynb`. Cả nhóm cùng viết phần tóm tắt cuối mục 3.2 (Key observations, Data quality issues, Preprocessing plan).
- **Thứ Sáu – Chủ Nhật (07–09/11):** Từng thành viên viết nháp đặc tả 2 câu hỏi mình phụ trách (Mục 3.3). Tạo các nhánh tính năng: `feature/q1-q2`, `feature/q3-q4`, `feature/q5-q6`.

---

### GIAI ĐOẠN 2: ĐẶC TẢ CÂU HỎI, TIỀN XỬ LÝ & PHÂN TÍCH BƯỚC ĐẦU (10/11 – 16/11)

#### 1. Bảng phân chia công việc Giai đoạn 2:
| Thành viên | Nhiệm vụ cụ thể trong Giai đoạn 2 | Sản phẩm bàn giao (Deliverables) | Người rà soát chéo |
| :--- | :--- | :--- | :---: |
| **TV1** *(Q1 & Q2)* | • Viết chi tiết đặc tả **Mục 3.3 cho Q1 và Q2** (Câu hỏi chuẩn xác, Target user, Motivation, Quyết định hỗ trợ).<br>• Khởi tạo module **`src/utils.py`**: Viết hàm tính tỷ lệ tự tử gộp đúng chuẩn ($100{,}000 \times \frac{\sum \text{ca}}{\sum \text{dân}}$), hàm kiểm tra tính đầy đủ của nhóm tuổi–giới.<br>• Thực hiện **tiền xử lý riêng cho Q1**: Lọc tập hợp quốc gia cố định (Fixed Cohort 1990–2015), in và giải thích số dòng trước/sau khi lọc.<br>• Thực hiện **tiền xử lý riêng cho Q2**: Ghép cặp Nam–Nữ theo `(country, year, age)`, tạo biến phái sinh $\text{Rate\_Diff}$ và $\text{Sex\_Ratio}$, in số dòng trước/sau.<br>• Dựng biểu đồ phân tích sơ bộ cho Q1 và Q2. | • Module `src/utils.py` ban đầu.<br>• Đặc tả chi tiết Q1, Q2 trong `notebooks/02_analysis_q1_q2.ipynb`.<br>• Báo cáo số dòng trước/sau các bước lọc.<br>• Bản nháp kết quả và 2 biểu đồ sơ bộ cho Q1, Q2. | **TV2** |
| **TV2** *(Q3 & Q4)* | • Viết chi tiết đặc tả **Mục 3.3 cho Q3 và Q4** (Target user, Motivation, Quyết định hỗ trợ).<br>• Khởi tạo module **`src/visualization.py`**: Thiết lập style biểu đồ Seaborn/Matplotlib chuẩn học thuật (font size, bảng màu đồng nhất, hàm lưu ảnh DPI cao).<br>• Thực hiện **tiền xử lý riêng cho Q3**: Gộp dữ liệu về cấp `(country, year)`, tạo biến trễ (lag 1 năm), tính tốc độ tăng trưởng $\% \Delta \text{GDP}$ và $\Delta \text{Rate}$, in số dòng trước/sau.<br>• Thực hiện **tiền xử lý riêng cho Q4**: Tách 2 giai đoạn (1995–2000 vs 2010–2015), chuẩn bị dữ liệu tính Tỷ lệ chuẩn hóa trực tiếp theo tuổi (ASR) với dân số chuẩn WHO, in số dòng trước/sau.<br>• Dựng biểu đồ phân tích sơ bộ cho Q3 và Q4. | • Module `src/visualization.py`.<br>• Đặc tả chi tiết Q3, Q4 trong `notebooks/02_analysis_q3_q4.ipynb`.<br>• Báo cáo số dòng trước/sau các bước gộp/lọc.<br>• Bản nháp kết quả và 2 biểu đồ sơ bộ cho Q3, Q4. | **TV3** |
| **TV3** *(Q5 & Q6)* | • Viết chi tiết đặc tả **Mục 3.3 cho Q5** (Non-ML) và **Q6** (Machine Learning).<br>• Thực hiện **tiền xử lý riêng cho Q5**: Thu thập file `country_region.csv`, thực hiện ghép dữ liệu (**Tiêu chí D1**) vào dataset chính, kiểm tra và báo cáo các khóa không khớp (unmatched keys), tạo biến cờ `is_missing_hdi` và biến sai lệch $\text{Bias}\%$, in số dòng trước/sau.<br>• Xây dựng khung bài toán **Machine Learning Q6**:<br>  - Ghép cặp năm $t$ với năm đích $t+1$ trên cùng quốc gia–tuổi–giới.<br>  - **Loại bỏ 100% các cột thuộc năm $t+1$** để chống rò rỉ dữ liệu.<br>  - Chia tập theo thời gian (**Time-based split**): Train (1990–2010) và Test (2011–2015).<br>  - Xây dựng mô hình cơ sở **Trivial Baseline** (Persistence: lấy tỷ lệ năm $t$ dự báo năm $t+1$).<br>  - Dựng khung `scikit-learn Pipeline` kết hợp Imputer + Scaler + OneHotEncoder. | • File dữ liệu ngoài `country_region.csv` và code merge kiểm tra khóa (D1).<br>• Đặc tả Q5 & Q6.<br>• `notebooks/02_analysis_q5.ipynb` có kết quả sơ bộ.<br>• `notebooks/03_ml_question.ipynb` có pipeline và điểm Baseline trên Train. | **TV1** |
| **Cả nhóm (3 người)** | • Họp giữa tuần rà soát: Đảm bảo quy tắc **BẮT BUỘC in số dòng trước/sau** sau mỗi bước thay đổi dữ liệu.<br>• Đảm bảo không ai chỉnh sửa chung 1 notebook trên cùng một nhánh Git để tránh xung đột.<br>• Đồng bộ code lên Git nhánh cá nhân (`feature/*`). | • Các nhánh Git cập nhật đều đặn.<br>• Hoàn thành mốc 50% khối lượng đồ án. | Cả nhóm |

#### 2. Kế hoạch hành động theo ngày (Day-by-Day):
- **Thứ Hai – Thứ Ba (10–11/11):** TV1 viết `src/utils.py`, TV2 viết `src/visualization.py`. Từng người viết code tiền xử lý riêng cho câu hỏi của mình, in số dòng trước/sau.
- **Thứ Tư – Thứ Năm (12–13/11):** Triển khai phân tích bước đầu: TV1 chạy Q1-Q2, TV2 chạy Q3-Q4, TV3 chạy Q5 ghép dữ liệu vùng miền (D1).
- **Thứ Sáu – Chủ Nhật (14–16/11):** TV3 dựng dataset Q6 ML, thực hiện Time-based split, chạy Baseline trên Train. Cả nhóm họp rà soát mốc bàn giao 16/11 (đạt bản nháp 6 câu).

---

### GIAI ĐOẠN 3: HOÀN THIỆN PHÂN TÍCH, TỐI ƯU HỌC MÁY & ĐÚC KẾT INSIGHT (17/11 – 23/11)

#### 1. Bảng phân chia công việc Giai đoạn 3:
| Thành viên | Nhiệm vụ cụ thể trong Giai đoạn 3 | Sản phẩm bàn giao (Deliverables) | Người rà soát chéo |
| :--- | :--- | :--- | :---: |
| **TV1** *(Q1 & Q2)* | • Hoàn thiện phân tích chuyên sâu cho **Q1**: Chạy kiểm tra tính vững (**D6**) khi đổi cửa sổ thời gian (1995–2014) và đổi ngưỡng cohort ($\ge 90\%$).<br>• Hoàn thiện phân tích chuyên sâu cho **Q2**: Chạy **Non-parametric Bootstrap** 1.000 lần theo cụm quốc gia để tính **Khoảng tin cậy 95% CI** cho mức chênh lệch Nam–Nữ ở từng độ tuổi (**D5**).<br>• Hoàn thiện **ít nhất 2 biểu đồ chuẩn học thuật/câu** (đủ title, axes labels, units, legend, cỡ mẫu $n$).<br>• Trả lời câu hỏi bằng số liệu định lượng cụ thể, nêu ý nghĩa thực tiễn và hạn chế.<br>• Khởi tạo sườn file `README.md`. | • File `notebooks/02_analysis_q1_q2.ipynb` hoàn thiện 100%.<br>• Tối thiểu 4 biểu đồ chuẩn học thuật cho Q1, Q2.<br>• Sườn file `README.md`. | **TV2** |
| **TV2** *(Q3, Q4 & Mục 3.5)* | • Hoàn thiện phân tích chuyên sâu cho **Q3**: Chạy kiểm tra tính vững (**D6**) với độ trễ 2 năm (lag 2) và loại bỏ các năm có cú sốc kinh tế $> 20\%$.<br>• Hoàn thiện phân tích chuyên sâu cho **Q4**: Đối chiếu kết quả ASR giữa bộ trọng số WHO Standard với bộ trọng số từ dữ liệu thực tế (**D6**). Tính % biến động tỷ lệ do già hóa dân số.<br>• Hoàn thiện **ít nhất 2 biểu đồ chuẩn/câu** cho Q3 và Q4.<br>• Chủ trì soạn thảo **Mục 3.5: Summary and Reflection**:<br>  - **Key findings:** Tổng hợp 3–5 phát hiện cốt lõi từ cả 6 câu, nhấn mạnh điểm gây bất ngờ nhất.<br>  - **Limitations:** Giới hạn của dữ liệu và phương pháp.<br>  - **Future work:** Hướng mở rộng nghiên cứu tương lai. | • File `notebooks/02_analysis_q3_q4.ipynb` hoàn thiện 100%.<br>• Tối thiểu 4 biểu đồ chuẩn học thuật cho Q3, Q4.<br>• Bản thảo hoàn chỉnh Mục 3.5 (Key findings, Limitations, Future work). | **TV3** |
| **TV3** *(Q5 & Q6)* | • Hoàn thiện **Q5**: Thực hiện kiểm định thống kê hai mẫu Kolmogorov-Smirnov / t-test (**D5**), phân tích mức sai lệch $\text{Bias}\%$ theo độ tuổi và vùng địa lý (**D4**). Vẽ $\ge 2$ biểu đồ chuẩn.<br>• Hoàn thiện bài toán **Machine Learning Q6**:<br>  - Tinh chỉnh siêu tham số (**Hyperparameter Tuning**) cho Ridge Regression và Random Forest Regressor bằng `TimeSeriesSplit` (5 folds) **chỉ trên tập Train**.<br>  - Đánh giá trên tập Test **đúng 1 lần duy nhất** bằng **MAE & RMSE**; giải thích lý do chọn MAE.<br>  - Thực hiện **Phân tích lỗi (Error Analysis)**: Khảo sát sai số theo nhóm tuổi, giới tính và trích xuất các mẫu sai lệch lớn nhất.<br>  - Sử dụng **Permutation Feature Importance** (XAI) để giải thích mô hình và trả lời tường minh câu hỏi gốc bằng mức chênh lệch MAE so với Baseline. | • File `notebooks/02_analysis_q5.ipynb` hoàn thiện 100% (kèm $\ge 2$ biểu đồ).<br>• File `notebooks/03_ml_question.ipynb` hoàn thiện 100%, chạy thông suốt không lỗi (kèm $\ge 3$ biểu đồ ML). | **TV1** |
| **Cả nhóm (3 người)** | • **Từng thành viên tự viết phần Phản tư cá nhân (Individual Reflection - Mục 3.5.4)**: Khó khăn gặp phải, cách giải quyết, bài học rút ra và minh bạch việc dùng LLM.<br>• Cập nhật đầy đủ các phiên trao đổi quan trọng vào `LLM_USAGE.md`.<br>• Họp nhóm tổng duyệt: Đảm bảo có đủ **ít nhất 12 biểu đồ chuẩn học thuật** toàn đồ án. | • 3 bản Phản tư cá nhân độc lập.<br>• File `LLM_USAGE.md` cập nhật đầy đủ.<br>• Toàn bộ 6 câu hỏi hoàn tất phân tích. | Cả nhóm |

#### 2. Kế hoạch hành động theo ngày (Day-by-Day):
- **Thứ Hai – Thứ Ba (17–18/11):** TV1 chạy Bootstrap CI Q2; TV2 chạy Robustness checks Q3 & Q4; TV3 chạy kiểm định Kolmogorov-Smirnov Q5. Chuẩn hóa biểu đồ.
- **Thứ Tư – Thứ Năm (19–20/11):** TV3 tinh chỉnh CV cho mô hình ML trên Train, đánh giá Test 1 lần, chạy Error Analysis và Permutation Importance.
- **Thứ Sáu – Thứ Bảy (21–22/11):** TV2 soạn thảo Key findings và Limitations; cả 3 người tự viết Individual Reflection; TV3 cập nhật `LLM_USAGE.md`.
- **Chủ Nhật (23/11):** Họp nhóm kiểm tra chéo toàn bộ kết quả của 6 câu hỏi và chuẩn bị sang giai đoạn đóng gói.

---

### GIAI ĐOẠN 4: ĐÓNG GÓI TÁI LẬP, THIẾT KẾ SLIDE, TẬP BẢO VỆ & KHÓA NỘP (24/11 – 29/11)

#### 1. Bảng phân chia công việc Giai đoạn 4:
| Thành viên | Nhiệm vụ cụ thể trong Giai đoạn 4 | Sản phẩm bàn giao (Deliverables) | Người rà soát chéo |
| :--- | :--- | :--- | :---: |
| **TV1** *(Trưởng nhóm)* | • Hoàn thiện file **`README.md`** chuẩn 100% rubric (Thành viên, MSSV, Task breakdown & Ownership, Dataset & License, **Declare existing work**, Danh sách 6 câu hỏi, Key findings, Hướng dẫn cài môi trường và chạy notebook theo thứ tự).<br>• Rà soát cấu trúc thư mục repo, dọn dẹp các file rác/file tạm.<br>• Kiểm tra lịch sử Git commit: Đảm bảo cả 3 thành viên đều có số commit tương xứng từ tài khoản cá nhân.<br>• Phụ trách nộp bài chính thức lên hệ thống môn học vào ngày 29/11. | • File `README.md` hoàn chỉnh 100%.<br>• Repo Git sạch, chuẩn quy cách đề bài.<br>• Biên nhận nộp bài thành công. | **TV2** |
| **TV2** | • **Chủ trì thiết kế Slide báo cáo (`slides.pdf`)**:<br>  - Chuẩn thời lượng thuyết trình: Đúng 15 phút (5 phút/người).<br>  - Thiết kế theo phong cách **Data Storytelling**: Đặt vấn đề $\rightarrow$ Câu hỏi $\rightarrow$ Trực quan hóa & Bằng chứng $\rightarrow$ Insight & Hành động thực tế.<br>  - **Tuyệt đối không copy code lên slide**.<br>• **Kiểm tra tính tái lập độc lập (Reproducibility Check)**: Tạo môi trường Conda hoàn toàn mới từ `environment.yml` trên máy cá nhân, chạy "Restart and Run All" toàn bộ 3 notebook để xác nhận không có lỗi phát sinh. | • File slide báo cáo hoàn thiện `slides.pdf`.<br>• Biên bản xác nhận kiểm tra tính tái lập độc lập (Reproducibility Passed). | **TV3** |
| **TV3** | • Rà soát và hoàn thiện file **`LLM_USAGE.md`**, đảm bảo tính toàn vẹn học thuật.<br>• **Chuẩn bị và điều phối buổi Vấn đáp thử (Mock Defense)**:<br>  - Soạn sẵn danh mục 15 câu hỏi phản biện (dựa trên Mục VI).<br>  - Bấm giờ thuyết trình 15 phút và chủ trì 10–15 phút chất vấn chéo code của nhau.<br>• Kiểm tra các file trung gian trong `data/processed/`, đảm bảo không commit file lớn trong `data/raw/`. | • File `LLM_USAGE.md` hoàn chỉnh.<br>• Danh mục câu hỏi Mock Q&A.<br>• Biên bản ghi nhận lỗi cần sửa sau buổi vấn đáp thử. | **TV1** |
| **Cả nhóm (3 người)** | • Tham gia buổi thuyết trình và vấn đáp thử nghiêm túc (Mock Defense).<br>• Sửa nhanh các lỗi phát hiện khi tập dượt.<br>• Merge tất cả các nhánh vào `main`.<br>• **KHÓA BẢN NỘP CHÍNH THỨC TRƯỚC 23:59 NGÀY 27/11/2026**.<br>• Ngày 28/11: Buffer dự phòng sự cố.<br>• Ngày 29/11: Nộp link repo và tài liệu trước giờ đóng cổng. | • Bản nộp chính thức được khóa an toàn đúng hạn.<br>• Cả 3 thành viên tự tin bảo vệ đồ án. | Cả nhóm |

#### 2. Kế hoạch hành động theo ngày (Day-by-Day):
- **Thứ Hai (24/11):** TV1 hoàn thiện `README.md`. TV2 tạo môi trường sạch chạy lại toàn bộ notebook kiểm tra Reproducibility. TV3 rà soát `LLM_USAGE.md`.
- **Thứ Ba (25/11):** TV2 hoàn tất thiết kế và xuất file `slides.pdf`. Từng thành viên chuẩn bị bài nói 5 phút của mình.
- **Thứ Tư (26/11):** Tổ chức buổi **Mock Defense nội bộ** (15 phút thuyết trình + 10 phút hỏi đáp chéo). Ghi nhận và sửa lỗi ngay trong tối 26/11.
- **Thứ Năm (27/11):** Kiểm tra lần cuối toàn bộ repo và **KHÓA BẢN NỘP TRƯỚC 23:59**.
- **Thứ Sáu (28/11):** Ngày dự phòng sự cố kỹ thuật.
- **Thứ Bảy (29/11):** Nộp bài chính thức lên portal môn học.

---

## VI. BỘ CÂU HỎI PHẢN BIỆN NỘI BỘ (MOCK Q&A) CHUẨN BỊ VẤN ĐÁP

Theo quy định đề thi, giảng viên có thể hỏi **bất kỳ thành viên nào về bất kỳ phần nào** của đồ án (kể cả phần do bạn khác làm) để chấm điểm cá nhân. Dưới đây là 10 câu hỏi trọng tâm cả 3 thành viên bắt buộc phải nắm vững:

1. **Về xử lý tỷ lệ (TV1 & Cả nhóm):** *Tại sao khi tính tỷ lệ tự tử của một quốc gia hoặc toàn cầu, nhóm không được lấy trung bình cộng của cột `suicides/100k pop` có sẵn mà phải tính lại bằng tổng số ca chia tổng dân số?*
   - *Trả lời:* Vì dân số giữa các phân nhóm tuổi–giới và giữa các quốc gia có sự chênh lệch cực lớn. Lấy trung bình cộng của tỷ lệ sẽ vô tình gán trọng số ngang nhau cho nhóm dân số 10.000 người và nhóm 100 triệu người, gây ra sai số trầm trọng (Simpson's Paradox).
2. **Về thiên lệch chọn mẫu (TV1):** *Trong Q1, tại sao kết quả xu hướng của mẫu đầy đủ (All Available) lại khác với mẫu cố định (Fixed Cohort)? Hiện tượng gì đã xảy ra?*
   - *Trả lời:* Do số lượng quốc gia nộp báo cáo cho WHO thay đổi theo từng năm. Những năm sau có nhiều quốc gia đang phát triển tham gia ghi nhận, vốn có tỷ lệ tự tử nền thấp hơn, làm cho đường xu hướng của mẫu đầy đủ dốc xuống giả tạo.
3. **Về phương pháp Bootstrap (TV1):** *Trong Q2, tại sao nhóm lại bootstrap lấy mẫu lại theo cấp quốc gia (Cluster Bootstrap) thay vì lấy mẫu lại từng dòng riêng lẻ?*
   - *Trả lời:* Vì các dòng trong cùng một quốc gia có tính phụ thuộc lẫn nhau (tương quan nội cụm). Nếu lấy mẫu lại từng dòng riêng lẻ sẽ vi phạm giả định quan sát độc lập và làm khoảng tin cậy bị thu hẹp giả tạo (quá lạc quan).
4. **Về kiểm soát biến gây nhiễu (TV2):** *Trong Q3, làm thế nào nhóm kiểm soát được các yếu tố văn hóa, tôn giáo cố định của từng nước khi đánh giá tác động của GDP?*
   - *Trả lời:* Nhóm sử dụng phương pháp sai phân bậc nhất (First-difference), chỉ so sánh sự biến thiên liên năm $(\Delta \text{GDP}$ và $\Delta \text{Rate})$ trong nội bộ từng quốc gia. Các đặc tính cố định theo thời gian của quốc gia đã tự động bị triệt tiêu qua phép trừ.
5. **Về kỹ thuật chuẩn hóa dân số (TV2):** *Trong Q4, giải thích trực giác vì sao tỷ lệ thô có thể tăng trong khi tỷ lệ chuẩn hóa (ASR) lại giảm?*
   - *Trả lời:* Do hiện tượng già hóa dân số. Người cao tuổi có tỷ lệ tự tử cao hơn nhóm trẻ. Dù công tác phòng chống tự tử ở từng nhóm tuổi đều đạt hiệu quả (tỷ lệ từng nhóm giảm), nhưng vì tỷ trọng người già trong dân số tăng vọt làm cho tỷ lệ bình quân chung toàn xã hội (tỷ lệ thô) bị kéo tăng lên.
6. **Về cơ chế khuyết thiếu (TV3):** *Trong Q5, dữ liệu HDI bị thiếu theo cơ chế nào (MCAR, MAR, hay MNAR)? Bằng chứng từ biểu đồ là gì?*
   - *Trả lời:* Không phải Missing Completely at Random (MCAR) vì việc thiếu phụ thuộc vào mốc thời gian (trước 2010 UNDP chỉ công bố 5 năm một lần) và phụ thuộc vào trình độ phát triển của quốc gia (các nước nghèo ít có khả năng thu thập dữ liệu HDI đầy đủ). Phân tích complete-case sẽ gây ra thiên lệch chọn lọc hướng về các nước phát triển.
7. **Về phòng chống rò rỉ dữ liệu (TV3 & Cả nhóm):** *Trong bài toán ML Q6, nhóm đã làm gì để đảm bảo 100% không bị Data Leakage?*
   - *Trả lời:* Nhóm loại bỏ hoàn toàn mọi cột thuộc về năm đích $t+1$; chia tập Train/Test theo trục thời gian (Time-based split, không dùng random split); toàn bộ quá trình Imputer, Scaler, Encoder được đóng gói trong scikit-learn Pipeline và chỉ fit trên tập Train.
8. **Về việc chọn Trivial Baseline (TV3):** *Tại sao trong Q6 nhóm chọn Baseline là tỷ lệ năm trước (Persistence) mà không phải là trung bình toàn bộ tập train?*
   - *Trả lời:* Tỷ lệ tự tử có tính tự tương quan chuỗi thời gian (Autocorrelation) rất cao giữa 2 năm liền kề. Dự đoán bằng giá trị năm trước là một baseline tự nhiên và có tính thách thức cao hơn nhiều so với việc chỉ lấy giá trị trung bình toàn cục.
9. **Về thước đo MAE vs RMSE (TV3):** *Tại sao nhóm chọn MAE làm thước đo đánh giá chính cho mô hình ML?*
   - *Trả lời:* MAE có cùng đơn vị với biến đích (số ca trên 100k dân), dễ diễn giải trực tiếp cho cơ quan y tế. Ngoài ra, dataset có một số ngoại lệ do các quốc gia nhỏ dân số ít biến động mạnh, RMSE sẽ phạt bình phương các lỗi này quá mức và làm lệch hướng tối ưu hóa mô hình.
10. **Về tính giải thích của mô hình (TV3):** *Từ kết quả Permutation Importance, đặc trưng nào mang lại giá trị dự báo lớn nhất cho năm $t+1$?*
    - *Trả lời:* Tỷ lệ ghi nhận tại năm $t$ và nhóm tuổi–giới tính là các đặc trưng có tầm quan trọng áp đảo, vượt trội hơn các chỉ số kinh tế vĩ mô như GDP trong ngắn hạn 1 năm.

---

## VII. NGUYÊN TẮC QUẢN TRỊ KỸ THUẬT & TRÁNH XUNG ĐỘT (GIT RULES)

1. **Quy tắc làm việc trên nhánh Git (Feature Branch Workflow):**
   - Không ai được commit trực tiếp vào nhánh `main`.
   - Mỗi người làm việc trên nhánh tính năng riêng: `feature/q1-q2`, `feature/q3-q4`, `feature/q5-q6`.
   - Chỉ merge vào nhánh chính thông qua Pull Request (PR) sau khi có ít nhất 1 thành viên khác review và phê duyệt.
2. **Quy tắc tránh xung đột tệp Jupyter Notebook (`.ipynb`):**
   - Tuyệt đối không để nhiều người cùng chỉnh sửa một file notebook cùng lúc trên Git.
   - Trong giai đoạn phân tích tuần 2 và 3, tách riêng các notebook độc lập:
     - `notebooks/02_analysis_q1_q2.ipynb` (TV1 làm chủ)
     - `notebooks/02_analysis_q3_q4.ipynb` (TV2 làm chủ)
     - `notebooks/02_analysis_q5.ipynb` & `notebooks/03_ml_question.ipynb` (TV3 làm chủ)
   - Trước khi commit bất kỳ notebook nào lên GitHub, luôn chọn lệnh **Clear All Outputs** nếu chỉ thay đổi nhỏ để tránh lưu trữ dung lượng lớn và gây xung đột metadata JSON.
3. **Mô-đun hóa mã nguồn (`src/`):**
   - Tuyệt đối không copy-paste các đoạn code dài giữa các notebook.
   - Đưa hàm xử lý số liệu vào `src/utils.py`.
   - Đưa hàm cấu hình vẽ biểu đồ vào `src/visualization.py`.
   - Trong notebook chỉ `import` và gọi hàm ngắn gọn, tăng tính chuyên nghiệp và thẩm mỹ khi chấm điểm.
4. **Cam kết liêm chính học thuật (Academic Integrity & AI Policy):**
   - Được phép dùng LLM (ChatGPT, Claude, Gemini) để giải thích khái niệm, sửa lỗi code, gợi ý cú pháp thư viện.
   - **Tuyệt đối không dùng LLM để viết thay phần nhận xét insight, kết luận hoặc phản tư cá nhân.**
   - Mọi lần dùng LLM đáng kể phải được ghi chép trung thực vào `LLM_USAGE.md` (công cụ, prompt, cách nhóm điều chỉnh/áp dụng).
   - Từng thành viên phải tự commit code từ tài khoản GitHub của chính mình để giảng viên đối chiếu lịch sử đóng góp khi chấm điểm cá nhân.

---

## VIII. BẢNG KIỂM TOÀN DIỆN TRƯỚC KHI KHÓA BẢN NỘP (SUBMISSION CHECKLIST)

Bảng kiểm rà soát cuối cùng trước 23:59 ngày 27/11/2026:

### 1. Về Cấu trúc thư mục & Mã nguồn:
- [ ] Repo chứa đầy đủ: `README.md`, `environment.yml`, `LLM_USAGE.md`, `slides.pdf`, `data/raw/`, `data/processed/`, `src/`, `notebooks/`.
- [ ] File `data/raw/` không bị commit dữ liệu dung lượng lớn lên GitHub (đã thiết lập `.gitignore`).
- [ ] Môi trường `environment.yml` sạch, cài đặt thành công trên hệ điều hành khác mà không bị lỗi xung đột package.
- [ ] Toàn bộ các notebook chạy tuần tự từ trên xuống dưới thành công thông qua lệnh **Restart Kernel and Run All Cells** (không có lỗi runtime).

### 2. Về Nội dung Học thuật & Phân tích:
- [ ] Mục 3.1: Đủ 5 phần (Subject, Source, License, Collection method, Motivation) và trích dẫn notebook tham khảo.
- [ ] **Declare existing work (BẮT BUỘC theo đề PDF):** README liệt kê rõ các public notebook/phân tích có sẵn trên Kaggle về dataset này, và giải thích cụ thể nhóm khác biệt ở điểm nào (câu hỏi khác, phương pháp sâu hơn, chuẩn hóa tuổi, ML dự báo thời gian). Reusing without attribution = plagiarism.
- [ ] Mục 3.2: Khám phá sâu các cột trọng tâm, kết thúc bằng 3 mục bắt buộc: 3–5 Key observations, Serious data quality issues, Preprocessing plan.
- [ ] Mục 3.3: Đủ 6 câu hỏi ($2 \times 3$), mỗi người sở hữu chính 2 câu, có đầy đủ Động cơ và Quyết định.
- [ ] 5 câu Non-ML: Phủ đầy đủ cả 6 tiêu chí chiều sâu D1, D2, D3, D4, D5, D6 (đạt tối đa — đề yêu cầu tối thiểu ≥4/6, mỗi câu ≥2 tiêu chí). Đặc biệt D1 được thỏa mãn trong Q5 (ghép bảng phân loại khu vực địa lý từ nguồn ngoài).
- [ ] Câu hỏi ML (Q6): Có đối tượng sử dụng rõ ràng; loại bỏ 100% rò rỉ dữ liệu; chia tập time-based; so sánh Baseline + Ridge + Random Forest; toàn bộ tiền xử lý nằm trong Pipeline; tinh chỉnh CV chỉ trên train; test đúng 1 lần; có Error Analysis và Permutation Feature Importance.
- [ ] Mục 3.4: Sau mỗi bước biến đổi dữ liệu (lọc, ghép, xóa) đều có code in và giải thích số dòng trước/sau.
- [ ] Biểu đồ: Có ít nhất 12 biểu đồ chuẩn học thuật (mỗi câu hỏi $\ge 2$ hình), có đầy đủ Title, X/Y-label, Units, Legend, và cỡ mẫu $n$.
- [ ] Mục 3.5: Đầy đủ 3–5 Key findings (nêu bật điểm bất ngờ nhất), Limitations, Future work, và phần Phản tư cá nhân (Individual Reflection) riêng biệt của từng thành viên.

### 3. Về Báo cáo & Thuyết trình:
- [ ] File `slides.pdf` đã xuất bản hoàn thiện, thiết kế dạng Data Storytelling, không chứa code.
- [ ] Phân chia thời lượng nói chuẩn xác 15 phút (5 phút/người).
- [ ] Đã tổ chức ít nhất 1 buổi Vấn đáp thử (Mock Defense) 25 phút để luyện tập trả lời chéo câu hỏi của nhau.
- [ ] Kiểm tra lịch sử Git: Cả 3 thành viên đều có số commit tương xứng từ tài khoản cá nhân.
- [ ] Xác nhận liên kết repo ở chế độ Public hoặc đã add quyền truy cập cho giảng viên trước giờ nộp bài.

---
*Kế hoạch này là kim chỉ nam chính thức cho nhóm 3 thành viên trong suốt quá trình thực hiện đồ án môn học CSC17104. Mọi thành viên cam kết tuân thủ nghiêm túc các mốc thời gian và tiêu chuẩn chất lượng đã đề ra.*
