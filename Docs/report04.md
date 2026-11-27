# Báo cáo tiến độ 04: chuẩn hóa Q5, Q6 theo khung chung của nhóm

**Người làm:** Nguyễn Đỗ Bảo Kiên (TV3), MSSV 24122039
**Ngày:** 27/11/2026
**Nhánh:** `feat/kien/q5-q6`

---

## 1. Tóm tắt

Q5 (`02_analysis.ipynb`) và Q6 (`03_ml_question.ipynb`) đã được sắp lại theo khung của Q1–Q2, theo hướng dẫn rà soát ngày 26/11. **Code và số liệu không đổi.**

| Việc | Trạng thái |
|---|---|
| Ô tiêu đề `CÂU HỎI NGHIÊN CỨU 5/6` (người phụ trách, tiêu chí, người dùng, quyết định hỗ trợ) | Xong |
| Bốn mục: 1. Tiền xử lý → 2. Phân tích → 3. Trực quan hóa → 4. Thảo luận | Xong |
| Tách code vẽ Hình Q5.1–Q5.4, Q6.1–Q6.3 khỏi code tính toán | Xong |
| Bỏ ngôi thứ nhất ("em") trong markdown của Q5, Q6 | Xong |
| `check_row_count` cho bước lọc 10 năm có HDI | Xong: 27,660 → 9,276 dòng (−66.46%) |
| `%matplotlib inline` lên dòng đầu ô import của `03_ml_question.ipynb` | Xong |
| `LLM_USAGE.md` dòng 07, 08 | Xong |
| Mục 4 Thảo luận Q5, Q6 (khung a–d đã có) | **Kiên đang viết** |
| Individual Reflection 3.5.4 | **Kiên đang viết** |

---

## 2. Kiểm tra sau khi sửa

- Chạy Restart & Run All cả 2 notebook trong `min_ds-env`: **0 lỗi, 0 cảnh báo**. `02` mất 83 giây, `03` mất 193 giây. `execution_count` liên tục.
- So output văn bản với bản trước khi sửa: **trùng hoàn toàn**. Khác biệt duy nhất là dòng `check_row_count` mới. Vẫn đủ 4 hình của Q5 và 3 hình của Q6.
- Các cell của người khác giữ nguyên: cell 0–5 và cell 3.5 của `02_analysis.ipynb`, cell 0 của `03_ml_question.ipynb`. Riêng ô import (cell 1) của `03` có thêm dòng `%matplotlib inline` theo hướng dẫn rà soát.

---

## 3. Lưu ý khi merge vào `main`

| # | Vấn đề | Cách xử lý đề xuất | Người |
|---|---|---|---|
| 1 | Ghép `feat/kien/q5-q6` với `feature/analysis-huy` | Đã thử bằng `git merge-tree`: **không xung đột** | Huy |
| 2 | `feature/q3-q4` được tách từ bản **cũ** của nhánh Q5/Q6 (trước khi đổi tên nhánh ngày 25/11). Ghép với nhánh này sẽ xung đột ở `02_analysis.ipynb` và `03_ml_question.ipynb`. `02` đã xung đột ngay cả trước lần sửa này | Khi gỡ xung đột: phần Q5 của `02` và toàn bộ `03` lấy bản của `feat/kien/q5-q6`; phần Q3–Q4 lấy bản của Đăng. Đăng không sửa nội dung Q5, Q6 nên không mất gì | Huy, Đăng |
| 3 | `feature/q3-q4` còn chứa 3 commit cũ của Kiên (`205a7be`, `ae76b40`, `8f98551`). Nội dung trùng với `b9cf6c2`, `67cb674`, `2b2a9ff` trên nhánh mới, nhưng commit message cũ còn dòng `Co-Authored-By: Claude` | Nên rebase `feature/q3-q4` lên `main` và bỏ 3 commit này (hoặc squash khi merge), để lịch sử không bị lặp và Claude không hiện trong Contributors | Đăng, Huy |
| 4 | Các việc ở mục 3 của `report03.md` (README Key finding 4, key finding Q5, `*[ ]*` ở tên TV3, thư mục `Docs/`) | Kiên gửi câu chữ key finding Q5, Q6 sau khi viết xong thảo luận | Huy, Kiên |

---

## 4. Việc còn lại (hạn 23:59 hôm nay)

- [ ] Kiên viết mục 4 Thảo luận Q5 (`02_analysis.ipynb`, cell 29) và Q6 (`03_ml_question.ipynb`, cell 23).
- [ ] Kiên viết Individual Reflection 3.5.4.
- [ ] Kiên mở PR `feat/kien/q5-q6` → `main`: https://github.com/24122039Kien/HCMUS_HKD_program_for_data_scientists/compare/main...feat/kien/q5-q6
- [ ] Huy merge các nhánh theo mục 3, chạy lại 3 notebook trên `main`.

---

## 5. Ghi chú về dùng AI

Lần chuẩn hóa này do Claude Code thực hiện theo yêu cầu của em, ghi ở `LLM_USAGE.md` dòng 08. AI không viết nội dung thảo luận và phản tư.
