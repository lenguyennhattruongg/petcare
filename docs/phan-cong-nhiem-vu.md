# KẾ HOẠCH PHÂN CÔNG NHIỆM VỤ & LỘ TRÌNH 6 TUẦN (NHÓM 2)
**Học phần:** Lập trình Web (Mã HP: 012012103105)  
**Giảng viên hướng dẫn:** ThS. Trần Thịnh Mạnh Đức - UTH  
**Đồ án:** Hệ thống Quản trị & Đặt lịch Bệnh viện Thú y PetCare (PetCare Veterinary System)  

---

## 1. DANH SÁCH THÀNH VIÊN & PHÂN CHIA MODULE TRÁCH NHIỆM

| STT | Họ và Tên | MSSV | Vai trò chính | Thư mục Backend phụ trách | Thư mục Giao diện phụ trách |
| :---: | :--- | :---: | :--- | :--- | :--- |
| **1** | **Lê Nguyễn Nhật Trường** *(Trưởng nhóm)* | `082206010882` | **Architecture, Database & Auth** | `config/`<br>`app/models/`<br>`app/routes/auth.py` | `app/templates/auth/`<br>`app/templates/layouts/` |
| **2** | **Thành viên 2** | `...` | **Client Portal & Booking** | `app/routes/client.py` | `app/templates/client/` |
| **3** | **Thành viên 3** | `...` | **Doctor Portal & Records** | `app/routes/doctor.py` | `app/templates/doctor/` |
| **4** | **Thành viên 4** | `...` | **Staff Portal & Payment QR** | `app/routes/staff.py` | `app/templates/staff/` |
| **5** | **Thành viên 5** | `...` | **Pharmacy & Inventory** | `app/routes/pharmacy.py` | `app/templates/pharmacy/` |
| **6** | **Thành viên 6** | `...` | **Admin Management & Charts** | `app/routes/admin.py` | `app/templates/admin/` |

---

## 2. QUY TẮC LÀM VIỆC TRÊN GITHUB ĐỂ KHÔNG BỊ XUNG ĐỘT (MERGE CONFLICT)

1. **Quy tắc "Vùng an toàn":**
   * Mỗi thành viên **CHỈ ĐƯỢC PHÉP CHỈNH SỬA** trong file route và thư mục template được phân công.
   * Tuyệt đối không chỉnh sửa file của bạn khác nếu chưa trao đổi trong nhóm.
   * File dùng chung (`app/__init__.py`, `base.html`, `requirements.txt`, `config.py`) chỉ do **Trưởng nhóm** chỉnh sửa hoặc duyệt qua Pull Request.

2. **Quy tắc đặt tên nhánh (Branch):**
   * Cú pháp: `feature/<tên-bạn>-<tên-chức-năng>`
   * Ví dụ:
     * Thành viên 1: `feature/truong-auth-login`
     * Thành viên 2: `feature/member2-dat-lich-kham`
     * Thành viên 3: `feature/member3-kham-benh-ke-don`
     * Thành viên 4: `feature/member4-tiep-tan-vietqr`
     * Thành viên 5: `feature/member5-quan-ly-kho-thuoc`
     * Thành viên 6: `feature/member6-bieu-do-doanh-thu`

3. **Quy trình nộp code hàng tuần:**
   * **Bước 1:** `git pull origin dev` (để lấy code mới nhất về máy).
   * **Bước 2:** `git checkout -b feature/<tên-nhánh>` (tạo nhánh mới).
   * **Bước 3:** Viết code, kiểm tra chạy tốt trên máy cá nhân.
   * **Bước 4:** `git add .` và `git commit -m "[TVx] Hoan thanh tinh nang xyz"`
   * **Bước 5:** `git push origin feature/<tên-nhánh>`
   * **Bước 6:** Lên GitHub tạo **Pull Request (PR)** gửi vào nhánh `dev`.
   * **Bước 7:** Trưởng nhóm vào kiểm tra và bấm nút **Merge**.

---

## 3. CHECKLIST CHI TIẾT TỪNG TUẦN CHO TỪNG THÀNH VIÊN

### TUẦN 1: KHỞI TẠO DỰ ÁN & PHÂN CÔNG (ĐÃ HOÀN THÀNH)
- [x] **Trưởng nhóm:** Tạo GitHub repo, thiết kế CSDL 23 bảng (`schema.sql` + `seed.sql`), dựng khung Flask App Factory.
- [x] **Trưởng nhóm:** Phân chia sườn thư mục cho 6 thành viên, viết tài liệu phân công.
- [ ] **Cả 6 thành viên:** Cài đặt Git, Python 3.12, clone repo về máy cá nhân và chạy thử thành công `python app.py`.

---

### TUẦN 2: HỆ THỐNG XÁC THỰC (AUTH) & GIAO DIỆN CƠ SỞ
- [ ] **Thành viên 1:**
  - [ ] Hoàn thiện logic đăng ký khách hàng (băm mật khẩu scrypt, lưu bảng `users` & `customers`).
  - [ ] Hoàn thiện đăng nhập (phân luồng theo vai trò: Admin, Bác sĩ, Tiếp tân, Khách hàng).
  - [ ] Chống tấn công giả mạo CSRF trên toàn bộ form.
- [ ] **Thành viên 2:** Dựng giao diện hoàn chỉnh cho trang chủ `client/home.html` và danh mục dịch vụ `client/services.html`.
- [ ] **Thành viên 3:** Dựng giao diện danh sách hàng đợi khám bệnh `doctor/queue.html`.
- [ ] **Thành viên 4:** Dựng giao diện màn hình tiếp nhận quầy `staff/checkin.html`.
- [ ] **Thành viên 5:** Dựng giao diện bảng danh mục thuốc `pharmacy/medicines.html`.
- [ ] **Thành viên 6:** Dựng giao diện bố cục 4 khối KPI và khung biểu đồ `admin/dashboard.html`.

---

### TUẦN 3: NGHIỆP VỤ ĐẶT LỊCH (CLIENT) & TIẾP NHẬN (STAFF)
- [ ] **Thành viên 2 (Client):**
  - [ ] Viết chức năng Khách hàng chọn ngày, chọn bác sĩ, chọn khung giờ khám.
  - [ ] Áp dụng quy tắc nghiệp vụ BR-02: Kiểm tra không cho phép đặt trùng khung giờ bác sĩ đã kín lịch.
  - [ ] Cho phép khách hàng thêm và quản lý hồ sơ bé cưng của mình (`client/my-pets.html`).
- [ ] **Thành viên 4 (Staff):**
  - [ ] Màn hình tiếp nhận tự động đồng bộ danh sách khách vừa đặt lịch online.
  - [ ] Bấm nút Check-in chuyển trạng thái ca khám từ `PENDING` sang `CHECKED_IN`.
  - [ ] Tiếp nhận khách vãng lai trực tiếp tại quầy không qua đặt trước.
- [ ] **Thành viên 1:** Hỗ trợ kết nối cơ sở dữ liệu SQLAlchemy cho TV2 và TV4.

---

### TUẦN 4: NGHIỆP VỤ BÁC SĨ (DOCTOR) & QUẢN LÝ KHO THUỐC (PHARMACY)
- [ ] **Thành viên 3 (Doctor):**
  - [ ] Màn hình khám bệnh: Nhập cân nặng, nhiệt độ, chẩn đoán triệu chứng, kết luận bệnh án.
  - [ ] Kê đơn thuốc: Chọn danh mục thuốc có sẵn trong kho, nhập liều lượng, số lượng viên/gói.
  - [ ] Chuyển trạng thái lịch hẹn sang `WAITING_FOR_PAYMENT`.
- [ ] **Thành viên 5 (Pharmacy):**
  - [ ] Chức năng thêm thuốc mới, cập nhật đơn giá, đơn vị tính.
  - [ ] Chức năng nhập kho thuốc theo lô hàng và hạn sử dụng (`pharmacy/import.html`).
  - [ ] Cảnh báo tự động các loại thuốc sắp hết hàng tồn kho.

---

### TUẦN 5: THANH TOÁN VIETQR & BÁO CÁO THỐNG KÊ (ADMIN)
- [ ] **Thành viên 4 (Staff):**
  - [ ] Tạo hóa đơn tự động từ dịch vụ khám + danh sách thuốc bác sĩ vừa kê.
  - [ ] Tích hợp API tạo mã **VietQR động** (Napas 247): Khi quét mã, ứng dụng ngân hàng tự động điền đúng số tiền và nội dung chuyển khoản.
  - [ ] Xác nhận thanh toán thành công, in hóa đơn / phiếu xuất viện.
- [ ] **Thành viên 5 (Pharmacy):**
  - [ ] Áp dụng quy tắc BR-08: Tự động trừ số lượng tồn kho nguyên tử ngay khi hóa đơn được thanh toán.
- [ ] **Thành viên 6 (Admin):**
  - [ ] Tích hợp thư viện Chart.js vẽ biểu đồ doanh thu theo 7 ngày gần nhất, theo tháng.
  - [ ] Thống kê top 5 dịch vụ khám nhiều nhất và tỷ lệ các loài thú cưng (chó/mèo/khác).
  - [ ] Màn hình quản lý phân quyền nhân sự (tạo tài khoản bác sĩ, lễ tân).

---

### TUẦN 6: KIỂM THỬ, DEPLOY CLOUD & BẢO VỆ ĐỒ ÁN
- [ ] **Cả 6 thành viên:**
  - [ ] Chạy thử kịch bản xuyên suốt: Đăng ký -> Đặt lịch -> Tiếp nhận -> Khám -> Kê đơn -> Thanh toán VietQR -> Xem biểu đồ.
  - [ ] Sửa các lỗi phát sinh (Fix bugs).
- [ ] **Trưởng nhóm:**
  - [ ] Triển khai website lên nền tảng đám mây (Render.com / PythonAnywhere) có tên miền và chứng chỉ HTTPS bảo mật.
  - [ ] Hợp nhất toàn bộ code từ nhánh `dev` vào nhánh `main`.
- [ ] **Cả nhóm:**
  - [ ] Hoàn thiện báo cáo đồ án Word / PDF theo mẫu trường ĐH Giao thông Vận tải TP.HCM (UTH).
  - [ ] Thiết kế Slide thuyết trình PowerPoint / Marp bảo vệ trước hội đồng.
