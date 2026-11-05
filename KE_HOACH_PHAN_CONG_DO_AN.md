# KẾ HOẠCH PHÂN CHIA CÔNG VIỆC ĐỒ ÁN CUỐI KỲ (CSC17104)
## MÔN: LẬP TRÌNH CHO KHOA HỌC DỮ LIỆU - HCMUS
**Bộ dữ liệu:** League of Legends Ranked Match Data – Season 15 (EUN) (68,300 dòng, 69 cột)  
**Quy mô nhóm:** 3 thành viên | **Thời gian hoàn thành:** 4 tuần (Đến ngày vấn đáp)

---

## I. TỔNG QUAN TIẾN ĐỘ 4 TUẦN (MASTER ROADMAP)

Để đảm bảo các thành viên cân bằng được với đồ án và kỳ thi của các môn học khác trong HK5, khối lượng công việc được rải đều theo chu trình chuẩn Data Science Workflow:

```
[Tuần 1: Thu thập & Khám phá dữ liệu]
  │   ├── Setup môi trường & Git
  │   ├── Mục 3.1: Data Collection & Motivation
  │   ├── Brainstorming & Chốt 6 câu hỏi định hướng
  │   └── Mục 3.2: Data Exploration (Phân tích đơn biến & đa biến)
  ▼
[Tuần 2: Hoàn thiện câu hỏi & Tiền xử lý + Phân tích chuyên sâu (Giai đoạn 1)]
  │   ├── Mục 3.3: Question Formulation (Đảm bảo tiêu chuẩn D1-D6 & ML)
  │   ├── Mục 3.4: Data Preprocessing & Baseline Analysis cho từng câu hỏi
  │   └── Tách code tái sử dụng vào thư mục src/
  ▼
[Tuần 3: Hoàn tất Phân tích, Huấn luyện ML & Đúc kết Insight]
  │   ├── Hoàn thiện trực quan hóa (≥ 2 plots/câu, chuẩn format học thuật)
  │   ├── Hoàn thiện ML Pipeline (Baseline, 2 Models, CV Tuning, Error Analysis, XAI)
  │   └── Mục 3.5: Summary, Key Findings, Limitations & Individual Reflection
  ▼
[Tuần 4: Đóng gói sản phẩm, Soạn Slide & Luyện tập Vấn đáp (Mock Defense)]
      ├── Tinh chỉnh Repo (README.md, environment.yml, LLM_USAGE.md)
      ├── Soạn Slide báo cáo (slides.pdf - 15 phút)
      └── Vấn đáp thử nghiệm nội bộ nhóm (10 phút Q&A)
```

---

## II. KẾ HOẠCH CHI TIẾT TUẦN 1: THU THẬP & KHÁM PHÁ DỮ LIỆU (EXPLORATION)

### 1. Phân bổ vai trò thành viên trong Tuần 1

| Thành viên | Vai trò chính trong Tuần 1 | Nhiệm vụ cụ thể |
| :--- | :--- | :--- |
| **Thành viên 1** *(Trưởng nhóm)* | **Data Architect & Cross-Column Lead** | • Quản lý Git Repository, cấu trúc thư mục, chuẩn hóa quy ước code.<br>• Viết toàn bộ **Mục 3.1 (Data Collection)** (trừ Motivation làm chung).<br>• Phụ trách **Overview của Mục 3.2** (Shape, ý nghĩa từng dòng, data types, drop logic ban đầu, duplicate check).<br>• Phụ trách **Relationships across multiple columns** (Ma trận tương quan, sanity checks đa biến).<br>• Review code và tổng hợp merge vào `01_collection_exploration.ipynb`. |
| **Thành viên 2** | **Data Explorer A (Combat & Economy)** | • Phụ trách khám phá chuyên sâu nhóm cột **Chỉ số thi đấu, Kinh tế, Sát thương & Trang bị**.<br>• Phân tích hình dạng phân phối (skewness, distribution shape, mean/median/IQR).<br>• Phát hiện outliers, giá trị vô lý, các trận đấu remake/đầu hàng sớm (< 15 phút).<br>• Đề xuất quy tắc xử lý/làm sạch nhóm cột số cho tuần 2. |
| **Thành viên 3** | **Data Explorer B (Meta, Rank & Objectives)** | • Phụ trách khám phá chuyên sâu nhóm cột **Bậc Rank, Thông thạo (Mastery), Vị trí, Tướng & Mục tiêu lớn**.<br>• Phân tích số lượng nhãn riêng biệt (distinct values), độ mất cân bằng (balance), lỗi chính tả, nhãn rỗng/placeholder (ví dụ `Item_0`).<br>• Phân tích cơ chế dữ liệu thiếu (Missing data) đặc biệt ở `flex_tier` (thiếu ~59%) và `solo_tier` (~1%).<br>• Đề xuất quy tắc nhóm danh mục hiếm (rare categories) và mã hóa dữ liệu. |
| **Cả nhóm (3 người)** | **Team Alignment** | • Thảo luận và thống nhất **Motivation** (Tại sao chọn dữ liệu LMHT Season 15 EUN?).<br>• Mỗi thành viên đưa ra **3 ý tưởng câu hỏi sơ bộ** (2 Non-ML, 1 ML) $\rightarrow$ Tổng 9 ý tưởng.<br>• Họp nhóm chọn ra **6 câu hỏi chủ chốt** (5 Non-ML, 1 ML) và xác định người phụ trách (mỗi người 2 câu).<br>• Tổng hợp **3–5 Key Observations, Data Quality Issues & Preprocessing Plan** để kết thúc Tuần 1. |

---

### 2. Bảng phân chia 69 trường (cột) dữ liệu trong bước Khám phá (3.2)

Dữ liệu gồm 68,300 dòng (tương ứng 6,830 trận đấu, mỗi trận 10 người chơi). Các cột được phân nhóm rõ ràng để không bị chồng chéo:

```
                                  TỔNG QUAN DỮ LIỆU (69 CỘT)
                                               │
      ┌────────────────────────────────────────┼────────────────────────────────────────┐
      ▼                                        ▼                                        ▼
 [THÀNH VIÊN 1: TỔNG QUAN & LIÊN KẾT]    [THÀNH VIÊN 2: COMBAT & ECONOMY]     [THÀNH VIÊN 3: METADATA & OBJECTIVES]
  • Metadata trận đấu:                     • Kết quả & Chỉ số cá nhân:          • Phân loại & Tướng:
    game_id, start_utc, duration,            win, kills, deaths, assists,         champion_id, champion_name,
    queue, platform_id, map_id,              kda_ratio, kill_participation        position
    game_mode, game_version                • Kinh tế & Sát thương:              • Xếp hạng & Thông thạo:
  • Kiểm tra toàn cục:                       gold_earned, gold_spent,             solo_tier, solo_rank, solo_lp,
    - Số dòng, số cột, kiểu dữ liệu          gold_per_min, damage_dealt,          solo_wins, solo_losses,
    - Trùng lặp (duplicate rows)             damage_per_min, damage_to_champ,     flex_tier, flex_rank, flex_lp,
    - Tổng hợp Missing Data toàn bảng        damage_champ_per_min, damage_taken   flex_wins, flex_losses,
  • Mối quan hệ đa biến (Cross-columns):   • Tầm nhìn:                          mastery_level, mastery_points,
    - Correlation matrix giữa các cụm        vision_score                         mastery_lastPlayTime,
    - Ghép nối cấp độ trận đấu             • Chỉ số cuối trận (Final Stats):     mastery_pointsSinceLastLevel,
      (Team Level Aggregation)               final_abilityHaste, final_armor,     mastery_pointsUntilNextLevel,
                                             final_attackDamage, final_health,    mastery_tokens
                                             final_attackSpeed, final_lifesteal, • Trang bị (Items - placeholder):
                                             final_movementSpeed,...              item0, item1, item2, item3,
                                                                                  item4, item5, item6
                                                                                • Mục tiêu đội (Team Objectives):
                                                                                  team_baronKills, team_dragonKills,
                                                                                  team_towerKills, team_champKills,
                                                                                  team_riftHeraldKills,
                                                                                  team_inhibitorKills
```

---

### 3. Gợi ý 9 ý tưởng câu hỏi sơ bộ và Định hướng 6 câu hỏi chuẩn đầu ra

Theo yêu cầu môn học, mỗi câu hỏi Non-ML phải thỏa mãn **ít nhất 2 tiêu chí chiều sâu** (trong các tiêu chí **D1–D6**), và cả đồ án phải phủ **ít nhất 4/6 tiêu chí**. Câu hỏi ML phải có người dùng rõ ràng, không bị **data leakage**, dùng `scikit-learn Pipeline`, so sánh Baseline + 2 mô hình, đánh giá Test set 1 lần kèm Phân tích lỗi và XAI.

#### A. Gợi ý 9 ý tưởng sơ bộ (Mỗi thành viên 3 ý tưởng để thảo luận):
- **Thành viên 1 đề xuất:**
  1. *(Non-ML)*: Việc kiểm soát Baron và Rồng tác động đến tỷ lệ thắng thế nào qua các mốc thời lượng trận đấu (Duration) và các bậc Rank? *(D3, D4, D5, D6)*
  2. *(Non-ML)*: Tỷ lệ chuyển hóa vàng thành sát thương (Gold-to-Damage efficiency) của các vị trí (Lane Positions) khác nhau ra sao giữa các bậc Rank? *(D3, D4, D5)*
  3. *(ML)*: Dự đoán thời lượng trận đấu (Match Duration: ngắn <20p, trung bình 20-35p, dài >35p) dựa trên chất tướng và bậc rank đội hình.
- **Thành viên 2 đề xuất:**
  4. *(Non-ML)*: Điểm tầm nhìn (`vision_score`) tác động như thế nào đến tỷ lệ tử vong và tỷ lệ thắng của vị trí Đi rừng và Hỗ trợ? *(D3, D4, D5)*
  5. *(Non-ML)*: Sự khác biệt về meta (tỷ lệ thắng, lượng sát thương, thời lượng trận) giữa các phiên bản cập nhật (Patch 15.1, 15.2, 15.3, 15.4)? *(D2, D3, D5)*
  6. *(ML)*: Dự đoán người chơi có đạt danh hiệu MVP / hiệu suất cao dựa trên các chỉ số giai đoạn đầu trận.
- **Thành viên 3 đề xuất:**
  7. *(Non-ML)*: Điểm thông thạo (`mastery_points`) có thực sự tỷ lệ thuận với tỷ lệ thắng và KDA của người chơi không, hay bị nhiễu bởi bậc Rank và độ khó tướng? *(D1, D3, D4, D5)*
  8. *(Non-ML)*: Chiến thuật đẩy lẻ (Phá trụ `team_towerKills`) so với giao tranh tổng (`team_champKills`) chiến thuật nào đảm bảo tỷ lệ thắng ổn định hơn khi bị dẫn trước về vàng? *(D3, D4, D5, D6)*
  9. *(ML)*: Dự đoán xác suất thắng trận (Match Outcome Prediction) ngay tại màn hình Cấm Chọn / Tải trận (Pre-game Draft) dựa trên đội hình, bậc rank và điểm thông thạo của 10 người chơi. *(Đạt chuẩn 100% không Data Leakage)*.

#### B. Khung 6 câu hỏi chính thức đề xuất chốt cho cả nhóm:

| Câu hỏi | Loại | Người sở hữu | Nội dung câu hỏi chi tiết | Tiêu chí chiều sâu thỏa mãn |
| :---: | :---: | :---: | :--- | :---: |
| **Q1** | Non-ML | **Thành viên 1** | **Ảnh hưởng của mục tiêu lớn (Baron, Dragon, Tower):** Sự chênh lệch kiểm soát mục tiêu lớn giữa hai đội ảnh hưởng như thế nào đến khả năng lật kèo hoặc chiến thắng, và xu hướng này có khác biệt giữa các mức thời lượng trận đấu (Early vs Late game) và bậc Rank không? | **D3** (Derived: Objective control diff, Game phase),<br>**D4** (Confounder: Duration, Rank),<br>**D5** (Bootstrap 95% CI, Chi-square test),<br>**D6** (Robustness: Lọc bỏ trận remake <15p). |
| **Q2** | Non-ML | **Thành viên 1** | **Hiệu suất chuyển hóa tài nguyên (Gold Efficiency):** Vị trí thi đấu nào (Top, Jungle, Mid, Bot, Sup) chuyển hóa vàng kiếm được thành sát thương lên tướng hiệu quả nhất, và hiệu suất này thay đổi thế nào khi người chơi leo lên các bậc xếp hạng cao hơn? | **D3** (Derived: Damage per Gold, Damage Share),<br>**D4** (Confounder: Position, Rank Tier),<br>**D5** (ANOVA / Kruskal-Wallis test, Effect size),<br>**D6** (Robustness: Lọc outlier sát thương do trận cù cưa). |
| **Q3** | Non-ML | **Thành viên 2** | **Tầm nhìn và Khả năng sống sót:** Mức độ đầu tư vào tầm nhìn (`vision_score`) có làm giảm tần suất bị hạ gục (`deaths`) và tăng cơ hội thắng của các vị trí nhạy cảm (Jungle, Support) hay không sau khi đã kiểm soát thời lượng trận và bậc xếp hạng? | **D3** (Derived: Vision per minute, Death rate),<br>**D4** (Confounder: Match duration, Rank Tier),<br>**D5** (Logistic Regression Odds Ratio, 95% CI),<br>**D6** (Robustness: Đánh giá riêng cho các trận cân bằng). |
| **Q4** | Non-ML | **Thành viên 2** | **Tác động của các bản cập nhật (Patch Shift):** Sự chuyển dịch giữa các phiên bản (Patch 15.1, 15.2, 15.3, 15.4 trong Season 15) đã làm biến động nhịp độ trận đấu (thời lượng trung bình) và ưu thế của các lớp tướng (AD Carry vs Pháp sư Mid) như thế nào? | **D2** (Reshaping & Time: Period-over-period across patches),<br>**D3** (Derived: Delta win rate/pick rate),<br>**D5** (Two-sample t-test / Mann-Whitney U test giữa các bản cập nhật),<br>**D6** (Robustness: So sánh Rank thấp vs Platinum+). |
| **Q5** | Non-ML | **Thành viên 3** | **Tương quan giữa Thông thạo (Mastery) và Năng lực thi đấu:** Điểm thông thạo tướng (`mastery_points`) phản ánh mức độ thành thạo kỹ năng thực tế (KDA, Winrate) đến mức nào, hay người chơi ở các bậc rank khác nhau tận dụng điểm thông thạo này theo cách khác nhau? | **D1** (Combining: Ghép thêm vai trò tướng từ Riot Data Dragon),<br>**D3** (Derived: Log-mastery, KDA ratio),<br>**D4** (Confounder: Solo Rank Tier, Lane),<br>**D5** (Kiểm định Spearman Correlation, hồi quy tuyến tính). |
| **Q6** | **ML** | **Thành viên 3** | **Dự đoán kết quả trận đấu tiền giao tranh (Pre-match Win Prediction):** Xây dựng mô hình phân lớp giúp người chơi/HLV dự đoán xác suất chiến thắng của đội ngay tại thời điểm kết thúc Cấm Chọn dựa trên thông tin đội hình, vị trí, bậc rank và điểm thông thạo của 10 người chơi *(Loại bỏ 100% chỉ số in-game để tránh Data Leakage)*. | **ML Requirements 1–6:**<br>• User: Người chơi/Analyst cân nhắc "Dodge" hoặc chọn lối đánh.<br>• Leakage: Drop toàn bộ in-game stats.<br>• Split: Time-based split theo `start_utc`.<br>• Baseline (50%) vs Logistic Regression vs LightGBM/Random Forest.<br>• Pipeline & CV Tuning.<br>• Error Analysis & Permutation Importance (XAI). |

---

### 4. Lịch trình hành động chi tiết trong Tuần 1 (Day-by-Day)

```
Thứ 2 - Thứ 3         Thứ 4                 Thứ 5 - Thứ 6         Thứ 7                 Chủ Nhật
┌──────────────┐      ┌──────────────┐      ┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│ Khởi tạo Git │ ───► │ Họp nhóm     │ ───► │ Độc lập thực │ ───► │ Họp tích hợp │ ───► │ Hoàn thiện   │
│ & Setup môi  │      │ Chốt 6 câu   │      │ hiện khám    │      │ & Review     │      │ Notebook 01  │
│ trường conda │      │ hỏi định     │      │ phá dữ liệu  │      │ chéo         │      │ & Kế hoạch   │
│ Viết mục 3.1 │      │ hướng        │      │ theo phân bổ │      │ (Merge code) │      │ Tuần 2       │
└──────────────┘      └──────────────┘      └──────────────┘      └──────────────┘      └──────────────┘
```

- **Thứ Hai – Thứ Ba (Ngày 1–2: Khởi động & Hoàn thành 3.1):**
  - Thành viên 1: Tạo repo GitHub, thiết lập file `.gitignore` (chặn commit file csv lớn trong `data/raw/`), tạo `environment.yml` mẫu. Viết mục **3.1 Data Collection** (Subject, Source, License, Collection method).
  - Cả 3 thành viên: Cùng soạn thảo phần **Motivation** (Lý do chọn LMHT S15, ý nghĩa thực tiễn với cộng đồng eSports và game thủ). Mỗi người chuẩn bị sẵn 3 ý tưởng câu hỏi (như mục 3 ở trên).
- **Thứ Tư (Ngày 3: Họp chốt câu hỏi & Phân chia công việc):**
  - Họp online/offline 45 phút. Thảo luận, chọn ra 6 câu hỏi chính thức (5 Non-ML, 1 ML) và xác định rõ owner của từng câu hỏi.
  - Phân nhóm cột cần explore sâu phục vụ trực tiếp cho các câu hỏi này.
- **Thứ Năm – Thứ Sáu (Ngày 4–5: Khám phá dữ liệu chuyên sâu theo phân công):**
  - Thành viên 2: Viết notebook phân tích nhóm cột Combat & Economy (vẽ histogram, boxplot kiểm tra outlier, xử lý duration < 15p, check tương quan gold vs damage).
  - Thành viên 3: Viết notebook phân tích nhóm cột Metadata, Rank, Mastery & Items (check tỷ lệ null của flex tier, phân bố tier solo, xử lý mã rỗng `Item_0`).
  - Thành viên 1: Viết phần Overview tổng quan toàn bộ 68,300 dòng và chạy phân tích tương quan tổng quát (Correlation heatmap, đa biến).
- **Thứ Bảy (Ngày 6: Ghép nối & Review chéo):**
  - Tạo Pull Request, Thành viên 1 chủ trì merge các đoạn phân tích của 3 người vào file chính: `notebooks/01_collection_exploration.ipynb`.
  - Cả nhóm review chéo: Đảm bảo code chạy trơn tru từ trên xuống dưới (Restart & Run All Kernel thành công không lỗi).
- **Chủ Nhật (Ngày 7: Đúc kết & Hoàn tất Tuần 1):**
  - Cả nhóm họp 30 phút: Cùng viết phần tóm tắt cuối mục 3.2: **3–5 Key observations**, **Serious data quality issues** (outliers, missingness, placeholder), và **Preprocessing plan** cho Tuần 2.
  - Ghi nhận việc sử dụng LLM vào file `LLM_USAGE.md`.

---

## III. ĐỀ XUẤT PHÂN CHIA CÔNG VIỆC CHO 3 TUẦN TIẾP THEO

Để các thành viên không bị quá tải khi bước vào cao điểm cuối kỳ, công việc từ Tuần 2 đến Tuần 4 được module hóa: mỗi người tự chủ động làm sâu 2 câu hỏi của mình, sau đó cùng nhau ráp nối thành sản phẩm hoàn chỉnh.

### 1. TUẦN 2: HOÀN THIỆN CÂU HỎI (3.3) & TIỀN XỬ LÝ + PHÂN TÍCH CHUYÊN SÂU (3.4)

*Trọng tâm: Chuyển từ khám phá sơ bộ sang thực hiện tính toán cụ thể cho 6 câu hỏi. Mỗi thành viên sở hữu 2 câu hỏi.*

| Thành viên | Nhiệm vụ chính trong Tuần 2 | Sản phẩm cần đạt (Deliverables) |
| :--- | :--- | :--- |
| **Thành viên 1** *(Q1 & Q2)* | • Viết chi tiết đặc tả cho **Q1** và **Q2** (động lực, người quan tâm, quyết định hướng tới).<br>• Thực hiện **tiền xử lý riêng** cho Q1 & Q2: tạo các biến phái sinh (`objective_diff`, `damage_per_gold`), lọc dữ liệu và in báo cáo số dòng trước/sau mỗi bước biến đổi.<br>• Phân tích thống kê: Chạy Bootstrap tính CI 95%, kiểm định Chi-square và ANOVA.<br>• Viết các hàm tiện ích dùng chung vào file `src/utils.py`. | • Hoàn thành 70% nội dung phân tích Q1 & Q2 trong notebook phân tích.<br>• Module `src/utils.py` khởi tạo. |
| **Thành viên 2** *(Q3 & Q4)* | • Viết chi tiết đặc tả cho **Q3** và **Q4**.<br>• Tiền xử lý dữ liệu chuỗi thời gian (`start_utc`), trích xuất Patch version, tính `vision_per_minute`. Báo cáo số dòng thay đổi qua từng bước.<br>• Phân tích so sánh biến động qua các phiên bản cập nhật (period-over-period) và phân tích tương quan điểm tầm nhìn với khả năng sống sót.<br>• Xây dựng module trực quan hóa dùng chung `src/visualization.py` (cấu hình seaborn/matplotlib đồng nhất font, palette màu, style). | • Hoàn thành 70% nội dung phân tích Q3 & Q4.<br>• Module `src/visualization.py` có hàm chuẩn vẽ đồ thị đẹp mắt. |
| **Thành viên 3** *(Q5 & Q6)* | • Viết chi tiết đặc tả cho **Q5** (Non-ML) và **Q6** (Machine Learning).<br>• Triển khai phân tích Q5: Ghép dữ liệu vai trò tướng (D1), biến đổi `log_mastery`, phân tích tương quan phân tầng theo Rank.<br>• Xây dựng khung bài toán ML cho Q6: Định nghĩa rõ Feature Space (chỉ lấy thông tin trước trận, loại bỏ 100% cột gây data leakage), thực hiện **Time-based split** (chia Train/Test theo mốc thời gian `start_utc`), xây dựng mô hình cơ sở Trivial Baseline (Tỷ lệ thắng 50%). | • Hoàn thành 70% nội dung phân tích Q5.<br>• Xong sườn Pipeline ML và Baseline model trong `notebooks/03_ml_question.ipynb`. |
| **Cả nhóm** | • Họp giữa tuần rà soát: Đảm bảo tổng thể 5 câu hỏi Non-ML phủ đủ ít nhất 4/6 tiêu chí (D1–D6).<br>• Đồng bộ code lên Git nhánh tính năng riêng của mỗi người (`feature/q1-q2`, `feature/q3-q4`, `feature/q5-q6`). | • Tránh xung đột code; tiến độ đúng hạn 50% đồ án. |

---

### 2. TUẦN 3: HOÀN TẤT PHÂN TÍCH, TỐI ƯU ML & TỔNG KẾT ĐÚC KẾT (3.4 & 3.5)

*Trọng tâm: Nâng cấp chất lượng đồ thị học thuật, hoàn thiện bài toán học máy và viết phần đúc kết, phản tư cá nhân.*

| Thành viên | Nhiệm vụ chính trong Tuần 3 | Sản phẩm cần đạt (Deliverables) |
| :--- | :--- | :--- |
| **Thành viên 1** *(Trưởng nhóm)* | • Hoàn thiện các biểu đồ cho Q1 & Q2: Đảm bảo mỗi câu hỏi có **ít nhất 2 biểu đồ chuẩn** (đầy đủ title, tên trục, đơn vị tính, chú thích legend, ghi rõ cỡ mẫu n).<br>• Viết diễn giải kết quả bằng số liệu cụ thể (không viết chung chung), nêu rõ ý nghĩa thực tế và hạn chế.<br>• Bắt đầu soạn thảo khung file `README.md` (Thông tin nhóm, mô tả bộ dữ liệu, cách cài đặt môi trường). | • Hoàn thiện 100% Q1 & Q2.<br>• Khung `README.md` hoàn chỉnh. |
| **Thành viên 2** | • Hoàn thiện các biểu đồ và số liệu diễn giải cho Q3 & Q4.<br>• Thực hiện kiểm tra tính vững (**Robustness checks - D6**): Chứng minh kết luận vẫn giữ nguyên khi đổi ngưỡng lọc outlier hoặc đổi khung thời gian.<br>• Chủ trì soạn thảo **Mục 3.5: Summary and Reflection** (Tổng hợp 3–5 Key Findings cốt lõi, điểm gây bất ngờ nhất, giới hạn của bộ dữ liệu và đề xuất hướng phát triển tương lai). | • Hoàn thiện 100% Q3 & Q4.<br>• Bản thảo mục 3.5 (Key findings, Limitations, Future work). |
| **Thành viên 3** | • Hoàn thiện 100% Q5 (Biểu đồ + kiểm định thống kê).<br>• Hoàn thiện bài toán Machine Learning (Q6):<br>  - Xây dựng trọn vẹn `Pipeline` trong scikit-learn (Imputer + OneHotEncoder + Scaler + Model).<br>  - Huấn luyện và tinh chỉnh siêu tham số (Cross-Validation trên tập Train) cho 2 mô hình (Logistic Regression và LightGBM / Random Forest).<br>  - Đánh giá trên tập Test đúng 1 lần (ROC-AUC, Precision, Recall, F1).<br>  - Thực hiện **Phân tích lỗi (Error Analysis)** trên các phân nhóm bị đoán sai và **Giải thích mô hình (Permutation Feature Importance / SHAP)**. | • Hoàn thiện 100% Q5 & Q6.<br>• File `notebooks/03_ml_question.ipynb` hoàn chỉnh, chạy sạch từ đầu đến cuối. |
| **Cả nhóm** | • Mỗi thành viên tự viết **Individual Reflection** (Mục 3.5.4): Những khó khăn gặp phải, cách vượt qua, bài học rút ra và minh bạch cách sử dụng công cụ LLM.<br>• Cập nhật chi tiết các câu prompt chính vào `LLM_USAGE.md`. | • Hoàn thiện mục Phản tư cá nhân và nhật ký LLM. |

---

### 3. TUẦN 4: ĐÓNG GÓI SẢN PHẨM, SOẠN SLIDE & TẬP LUYỆN VẤN ĐÁP

*Trọng tâm: Đảm bảo đồ án tái lập được (Reproducible), chuẩn bị slide kể câu chuyện dữ liệu (15 phút) và luyện vấn đáp cá nhân (10 phút).*

| Thành viên | Nhiệm vụ chính trong Tuần 4 | Sản phẩm cần đạt (Deliverables) |
| :--- | :--- | :--- |
| **Thành viên 1** *(Trưởng nhóm)* | • **Kiểm tra tính tái lập (Reproducibility Check):** Tạo môi trường ảo sạch từ file `environment.yml`, chạy lại toàn bộ notebook theo thứ tự: `01_collection_exploration.ipynb` $\rightarrow$ `02_analysis.ipynb` $\rightarrow$ `03_ml_question.ipynb`. Đảm bảo không còn lỗi đường dẫn hay thiếu thư viện.<br>• Hoàn thiện `README.md` theo đầy đủ các mục giảng viên yêu cầu.<br>• Rà soát Git Commit History của cả nhóm để đảm bảo đóng góp công bằng, commit message rõ ràng. | • Repo hoàn thiện 100%, sẵn sàng nộp bài.<br>• File `environment.yml` chuẩn hóa. |
| **Thành viên 2** | • **Chủ trì thiết kế Slide báo cáo (`slides.pdf`):**<br>  - Thời lượng thuyết trình: Chuẩn 15 phút.<br>  - Cấu trúc slide: Tập trung "Kể câu chuyện của dữ liệu" (Data Storytelling: Vấn đề $\rightarrow$ Câu hỏi $\rightarrow$ Trực quan hóa & Bằng chứng $\rightarrow$ Insight & Hành động thực tế). Tuyệt đối **không copy code lên slide**.<br>• Phân chia thời lượng nói: Mỗi thành viên trình bày đúng 5 phút về 2 câu hỏi mà mình phụ trách. | • File `slides.pdf` chuẩn thiết kế học thuật, trực quan, chuyên nghiệp. |
| **Thành viên 3** | • Rà soát toàn bộ file `LLM_USAGE.md` và kiểm tra tính toàn vẹn học thuật (Academic Integrity).<br>• Chuẩn bị **Bộ câu hỏi phản biện nội bộ (Mock Q&A):** Soạn sẵn danh sách 15 câu hỏi giảng viên có thể hỏi xoay quanh phương pháp thống kê, rò rỉ dữ liệu (leakage), độ tin cậy của mô hình, ý nghĩa các chỉ số.<br>• Đóng gói cấu trúc thư mục nộp bài chuẩn quy cách. | • File `LLM_USAGE.md` chi tiết.<br>• Danh sách câu hỏi Mock Q&A. |
| **Cả nhóm** | • **Tổ chức buổi Vấn đáp thử (Mock Defense):**<br>  - Nhóm bấm giờ thuyết trình thử 15 phút.<br>  - Dành 15-20 phút chất vấn chéo lẫn nhau về code của người khác viết (vì trong buổi thi thật, giảng viên có thể hỏi bất kỳ ai về bất kỳ phần nào của đồ án để cho điểm cá nhân).<br>• Nộp bài và sẵn sàng bảo vệ. | • Cả 3 thành viên tự tin nắm vững toàn bộ đồ án và code của nhau. |

---

## IV. NGUYÊN TẮC LÀM VIỆC NHÓM & QUẢN TRỊ RỦI RO (GIT & NOTEBOOK)

1. **Quy tắc làm việc với Jupyter Notebook trên Git (Tránh Merge Conflict):**
   - Không nhiều người cùng sửa chung một file `.ipynb` tại một thời điểm trên cùng một nhánh.
   - Trong quá trình phân tích ở Tuần 2 và Tuần 3, mỗi thành viên tạo notebook riêng:
     - `notebooks/02_analysis_q1_q2.ipynb` (Thành viên 1)
     - `notebooks/02_analysis_q3_q4.ipynb` (Thành viên 2)
     - `notebooks/02_analysis_q5.ipynb` & `notebooks/03_ml_question.ipynb` (Thành viên 3)
   - Sau khi code và biểu đồ đã ổn định, Trưởng nhóm sẽ phụ trách tổng hợp vào file `02_analysis.ipynb` chung hoặc giữ các file riêng theo câu hỏi (được phép theo mục 4 của đề cương: *"split per question if large"*).
   - Trước khi commit notebook lên Git, luôn chọn **Clear All Outputs** nếu chỉ thay đổi code nhỏ để tránh xung đột metadata dung lượng lớn.
2. **Quy tắc viết code mô-đun hóa (thư mục `src/`):**
   - Các hàm tính toán số liệu (ví dụ hàm tính bootstrap CI, hàm lọc trận đấu hợp lệ) viết vào `src/utils.py`.
   - Các hàm vẽ biểu đồ chuẩn quy cách viết vào `src/visualization.py`.
   - Trong notebook chỉ gọi hàm và hiển thị kết quả, giúp notebook sạch đẹp, dễ đọc cho giảng viên.
3. **Minh bạch sử dụng công cụ AI (LLM Policy):**
   - Được phép dùng LLM (ChatGPT, Claude, Gemini, Copilot) như một người hướng dẫn (Tutor) giải thích khái niệm, sửa lỗi thư viện hoặc gợi ý hàm.
   - Tuyệt đối không dùng LLM để viết thay toàn bộ phần nhận xét, phân tích insight hoặc phần phản tư cá nhân.
   - Mọi lần trao đổi quan trọng với LLM phải được ghi nhận vào `LLM_USAGE.md` (ghi rõ công cụ, câu hỏi và cách nhóm áp dụng/điều chỉnh).
4. **Chuẩn bị cho Điểm số Cá nhân (Individual Grading):**
   - Điểm số vấn đáp của từng cá nhân sẽ phụ thuộc vào:
     1. Khả năng tự trình bày mạch lạc 2 câu hỏi mình phụ trách.
     2. Khả năng trả lời câu hỏi vấn đáp của thầy cô về bất kỳ phần nào của đồ án (kể cả phần do bạn khác viết).
     3. Lịch sử commit trên Git (mỗi thành viên phải tự commit code và nội dung của mình từ tài khoản GitHub cá nhân, không để 1 người commit hộ).

---
*Kế hoạch này được thiết lập để đảm bảo chất lượng đồ án đạt mức tối đa theo thang điểm của FIT-HCMUS, đồng thời giữ tải làm việc hợp lý (~6-8 giờ/tuần/người).*

