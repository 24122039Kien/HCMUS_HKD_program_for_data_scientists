# Báo cáo tiến độ 01: phần EDA của TV3

**Người làm:** Nguyễn Đỗ Bảo Kiên (TV3), MSSV 24122039
**Ngày:** 09/11/2026
**Nhánh:** `feature/eda-kien`, tách từ `feature/eda-huy`

---

## 1. Tóm tắt

| Việc | Trạng thái | Vị trí |
|---|---|---|
| EDA cột `sex`, `age` (nhãn, cân bằng, đủ 12 phân nhóm) | Xong | Notebook `01`, mục 3.2.4 a |
| EDA cột `generation` (kiểm tra dư thừa) | Xong | Mục 3.2.4 b |
| EDA cột `HDI for year` (mức thiếu, cơ chế thiếu) | Xong | Mục 3.2.4 c |
| Đếm mẫu (t−1, t, t+1) và chia train/test cho Q6 | Xong | Mục 3.2.4 d |
| Tóm tắt phần TV3 cho mục 3.2 | Xong | Mục 3.2.4 e |
| Điền thông tin TV3 vào `README.md` | Xong | Commit `8458357` |
| Ghi nhật ký dùng AI của TV3 | Xong, chưa commit | `LLM_USAGE.md` mục 2.3 |
| Q5 (HDI thiếu + ghép `country_region.csv`) | Chưa làm | |
| Q6 (Ridge, Random Forest so với persistence) | Chưa làm | |

Phần EDA nằm ở `notebooks/01_collection_exploration.ipynb`, cell 16–40, gồm 25 cell mới và 5 biểu đồ. Cell placeholder TV1 để sẵn cho TV3 đã được thay. Các cell khác của TV1 giữ nguyên. Notebook đã chạy lại từ đầu đến cuối (Restart & Run All) trong môi trường `min_ds-env`, không lỗi, và mọi con số dưới đây lấy từ lần chạy đó.

---

## 2. Kết quả chính

### a) `sex` và `age`

- Nhãn sạch, không có nhãn viết lệch: 2 giới, 6 nhóm tuổi. Mỗi giới có 13,910 dòng.
- 2,305 cặp (country, year) đủ 12 dòng. 16 cặp chỉ có 10 dòng, **tất cả ở năm 2016 và đều thiếu nhóm 5-14**.
- Tỷ lệ gộp (tổng số ca / tổng dân số × 100k): nam 20.71, nữ 5.94, gấp khoảng 3.5 lần.
- Hiệu nam − nữ lớn nhất ở nhóm 75+ (32.00/100k). Tỷ số nam/nữ lại lớn nhất ở nhóm 25-34 (4.32 lần). Vì vậy khi viết "chênh lệch giới" cần nói rõ đang dùng hiệu hay tỷ số.
- Nhóm 35-54 chiếm nhiều ca nhất (36.34%) chỉ vì đông dân (28.01% dân số). Tính theo tỷ lệ thì nhóm 75+ cao nhất (24.52/100k).

### b) `generation`

- Trong cả 191 tổ hợp (year, age), mỗi tổ hợp chỉ có đúng 1 nhãn thế hệ. Nghĩa là `generation` suy ra hoàn toàn từ `year` và `age`, nên **là biến dư thừa**.
- Khoảng năm sinh của các thế hệ chồng lấn nhau (Silent 1901–1955, Boomers 1937–1974), và nhãn đổi đột ngột theo năm.
- Đề xuất: **bỏ cột này khỏi Q6**. Cột không thêm thông tin mà còn ngầm mã hóa giai đoạn thời gian; ví dụ Generation Z chỉ xuất hiện từ năm 2007.

### c) `HDI for year`

- Thiếu 19,456/27,820 dòng, tức **69.94%**. README và kế hoạch đang ghi ~69.6%, cần sửa lại.
- HDI chỉ có ở 10 năm: 1985, 1990, 1995, 2000, 2005 và 2010–2014. Năm 2015 không có.
- Có 2 nguồn thiếu khác nhau:
  1. **Thiếu theo năm** (95.3% số dòng thiếu): những năm này không có số liệu HDI.
  2. **Thiếu theo nước** trong các năm có HDI: 76/773 cặp country-year, thuộc 24 nước. Trong đó 11 nước không bao giờ có HDI, có cả Nga (32.78/100k) và Hàn Quốc (19.32/100k).
- Trong các năm có HDI, nhóm bị thiếu khác hẳn nhóm có số liệu:

  | | GDP/người trung vị | Tỷ lệ gộp |
  |---|---|---|
  | Thiếu HDI | 7,239 USD | 25.93/100k |
  | Có HDI | 12,584 USD | 11.13/100k |

  Vậy HDI **không thiếu hoàn toàn ngẫu nhiên (không phải MCAR)**. Nếu bỏ các dòng thiếu thì kết quả sẽ bị lệch.
- HDI tương quan rất mạnh với log GDP/người: r = 0.913.

### d) Mẫu cho Q6

- Có 1,210 nhóm (country, sex, age), 25,926 cặp năm (t, t+1) liền nhau và 24,246 mẫu có đủ 3 năm liền nhau.
- Chuỗi năm bị đứt quãng 684 lần ở 39 nước. Vì vậy phải kiểm tra `year + 1` thật sự, không được chỉ dùng `shift`.
- Chia theo năm đích t+1:

  | Tập | Năm đích | Số mẫu | Số nước | % mẫu có HDI ở năm t |
  |---|---|---|---|---|
  | Train | 1990–2010 | 18,108 | 92 | 15.8% |
  | Test | 2011–2015 | 4,428 | 85 | 95.7% |

- Bị loại: 1,560 mẫu có năm đích trước 1990 và 150 mẫu có năm đích 2016.
- Nicaragua và Turkey chỉ có trong test, nên `OneHotEncoder` cần đặt `handle_unknown='ignore'`.
- Tương quan giữa tỷ lệ năm t và năm t+1 là 0.928 (chỉ tính trên train). Do đó mô hình persistence (đoán năm sau bằng năm nay) sẽ là baseline rất mạnh.

---

## 3. Đề xuất cho Q5 và Q6

- **Q5:** tách riêng 2 nguồn thiếu HDI. Phân tích chính chỉ dùng các năm có HDI. Ngoài tỷ lệ gộp (bị Nga chi phối vì Nga rất đông dân), báo cáo thêm trung vị theo quốc gia để kiểm tra độ vững (D6). Ghép `country_region.csv` để xem phần thiếu tập trung ở vùng nào (D1).
- **Q6:**
  - **Không dùng HDI làm đặc trưng.** Train chỉ có 15.8% mẫu có HDI, test có 95.7%, nên phân phối lệch giữa hai tập. GDP/người đã mang gần hết thông tin của HDI và không thiếu dòng nào.
  - Bỏ `generation`.
  - Loại năm 2016.
  - Bắt buộc so sánh với baseline persistence.

---

## 4. Lỗi phát hiện ở phần TV1 (mục 3.2.2, cell 13–14)

Gửi Huy rà lại:

1. Bảng top 10 bị NaN, do ghép 2 Series có index lệch nhau.
2. Nhận xét ghi "24 quốc gia có ≥ 30 năm", nhưng output cho ra 31.
3. Nhận xét ghi "65–80 nước/năm", nhưng số thực tế là 77–89.

---

## 5. Việc tiếp theo

- [ ] Huy review và merge PR `feature/eda-kien` → `feature/eda-huy`.
- [ ] Sửa con số 69.6% thành 69.94% trong README, kế hoạch và mục 3.1.
- [ ] Đánh số lại hình sau khi ghép phần của TV2.
- [ ] Làm Q5, rồi Q6, trên nhánh `feature/q5-q6`.

---

## 6. Ghi chú về dùng AI

Phần EDA này có dùng Claude Code. Chi tiết từng lần dùng, gồm cả việc AI viết code và nhận xét của mục 3.2.4, được ghi ở `LLM_USAGE.md` mục 2.3.
