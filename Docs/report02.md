# Báo cáo tiến độ 02: Q5 và Q6 của TV3

**Người làm:** Nguyễn Đỗ Bảo Kiên (TV3), MSSV 24122039
**Ngày:** 23/11/2026
**Nhánh:** `feature/q5-q6`, tách từ `origin/main` (commit `1e05dfd`)

---

## 1. Tóm tắt

| Việc (giai đoạn 2–3) | Trạng thái | Vị trí |
|---|---|---|
| Đặc tả Q5, Q6 (mục 3.3) | Xong | Đầu mục Q5 trong `02_analysis.ipynb`; đầu `03_ml_question.ipynb` |
| File ngoài `country_region.csv` và ghép bảng (D1) | Xong | `data/raw/country_region.csv` |
| Q5: tiền xử lý, phân tích D1–D6, 4 biểu đồ | Xong phần code | `02_analysis.ipynb`, ngay sau tiêu đề Q5 |
| Q6: dựng mẫu, CV, test, phân tích lỗi, XAI, 3 biểu đồ | Xong phần code | `03_ml_question.ipynb` |
| Phần kết quả và thảo luận của Q5, Q6 | **Kiên đang viết** | Ô "✍️ [TV3 tự viết]" cuối mỗi câu |
| Individual Reflection 3.5.4 | **Kiên đang viết** | |
| `LLM_USAGE.md` mục 2.3 | Cập nhật đến dòng 06 | |

Cả hai notebook đã chạy Restart & Run All trong conda (pandas 2.1.1, scikit-learn 1.3.1), không có lỗi hay cảnh báo. `02_analysis.ipynb` chạy khoảng 80 giây, phần lớn thời gian là cluster bootstrap; `03_ml_question.ipynb` chạy khoảng 3 phút 15 giây.

---

## 2. Kết quả chính

### Q5: HDI thiếu và độ lệch của complete-case

- Sau khi loại năm 2016 còn 27,660 dòng, 100 nước (Mongolia chỉ có năm 2016 nên bị loại theo).
- **D1:** có 11 tên nước không khớp với World Bank (ví dụ `Republic of Korea` so với `Korea, Rep.`). Sau khi chuẩn hóa bằng bảng ánh xạ, cả 11 đều khớp và số dòng giữ nguyên.
- **Hai nguồn thiếu:** 66.46% số dòng thiếu do cả năm đó không có HDI; 3.30% thiếu do nước đó không có HDI trong năm có HDI (76 cặp country-year). 9 nước không bao giờ có HDI, trong đó có Nga và Hàn Quốc.
- **Bias% của complete-case** trong 10 năm có HDI là **−12.24%** (12.68 → 11.13 ca/100k), KTC 95% cluster bootstrap từ −29.07% đến 0.18%.
- **Độ vững:** bỏ Nga thì Bias% còn −2.91%; bỏ 9 nước không bao giờ có HDI thì còn −0.03%. Mann-Whitney U giữa country-year thiếu và có HDI cho p = 0.43.

### Q6: dự báo tỷ lệ năm t+1

- Mẫu (t−1, t, t+1): train 18,108 mẫu (năm đích 1990–2010), test 4,428 mẫu (2011–2015).
- MAE CV (5 fold theo năm): persistence 2.867; Random Forest dự báo mức thay đổi 2.712 (tốt nhất, được chốt); Ridge dự báo mức thay đổi 2.716.
- **Test (một lần):** MAE 2.065 so với 2.213 của persistence (tốt hơn 6.68%), RMSE 4.848 so với 5.844 (tốt hơn 17.04%).
- Mô hình kém hơn persistence ở nhóm có tỷ lệ năm t thấp (< 5) và ở nhóm 5-14 tuổi.

---

## 3. Thay đổi ở file chung (nhờ Huy xem khi review)

1. **`.gitignore`:** thêm dòng `!data/raw/country_region.csv`, để file vùng (218 dòng, khoảng 10 KB) được commit, giúp người khác chạy lại được Q5. `master.csv` vẫn bị bỏ qua như cũ.
2. **`02_analysis.ipynb`:** em chỉ **chèn thêm** 18 cell ngay sau tiêu đề Q5. Các cell Q1–Q4, 3.5 giữ nguyên; riêng cell import chung có thêm output và `execution_count` do chạy lại. Biến của Q5 đều có tiền tố `q5_` để không trùng với biến của Q1–Q4.
3. **Lưu ý khi merge:** TV1 và TV2 cũng sửa notebook này, nên chỗ tiếp giáp giữa Q4 và Q5 có thể bị xung đột JSON. Nên merge lần lượt từng nhánh và chạy lại notebook sau khi merge.
4. **Biểu đồ đầu tiên không hiện:** khi chạy bằng `nbconvert`, biểu đồ đầu tiên của notebook chỉ in ra `<Figure ...>`, không có hình. Em sửa bằng `%matplotlib inline` ở cell đầu của Q5 và Q6. Nếu Q1 vẽ hình trước Q5 mà gặp lỗi này, Huy có thể thêm dòng đó vào cell import chung.
5. Biểu đồ được lưu ở `data/processed/tv3_q5_*.png` và `tv3_q6_*.png` (theo cách nhóm đang dùng `save_figure`, không commit). TV2 có thể lấy để làm slide.

---

## 4. Việc còn lại

- [ ] Kiên viết phần kết quả và thảo luận của Q5, Q6 (ô "✍️ [TV3 tự viết]").
- [ ] Kiên viết Individual Reflection 3.5.4.
- [ ] Huy sửa con số "~69.6%" trong phần nhận xét đầu của notebook 01 thành 69.94%.
- [ ] Review và merge `feature/q5-q6` vào `main`.
- [ ] Giai đoạn 4: rà soát `LLM_USAGE.md`, soạn câu hỏi mock defense (26/11).

---

## 5. Ghi chú về dùng AI

Code và phần mô tả phương pháp của Q5, Q6 do Claude Code viết theo yêu cầu của em, đã chạy lại để kiểm chứng. Chi tiết ở `LLM_USAGE.md`, mục 2.3, dòng 05–06.
