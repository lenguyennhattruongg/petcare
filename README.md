# 🐾 PETCARE - HỆ THỐNG QUẢN TRỊ & ĐẶT LỊCH TRUNG TÂM THÚ Y

> **ĐỒ ÁN HỌC PHẦN: LẬP TRÌNH WEB (MÃ HP: 012012103105)**  
> **Trường Đại học Giao thông Vận tải TP.HCM (UTH)**  
> **Giảng viên hướng dẫn:** ThS. Trần Thịnh Mạnh Đức  
> **Nhóm thực hiện:** Nhóm 2 (6 thành viên)  
> **Trưởng nhóm:** Lê Nguyễn Nhật Trường - MSSV: `082206010882`  
> **GitHub Repository:** [https://github.com/lenguyennhattruongg/petcare](https://github.com/lenguyennhattruongg/petcare)

---

## 👥 1. BẢNG PHÂN CÔNG NHIỆM VỤ 6 THÀNH VIÊN

Dự án được thiết kế theo kiến trúc phân tầng độc lập (**Flask Blueprints**). Mỗi thành viên phụ trách trọn gói một phân hệ, sở hữu file route logic và thư mục giao diện riêng biệt, **tuyệt đối không gây xung đột code (merge conflict)**:

| STT | Họ và Tên | MSSV | Vai trò chính | Thư mục Backend phụ trách | Thư mục Template phụ trách | Mô tả công việc cụ thể |
| :---: | :--- | :---: | :--- | :--- | :--- | :--- |
| **1** | **Lê Nguyễn Nhật Trường**<br>*(Trưởng nhóm)* | `082206010882` | **Architecture, DevOps & Auth** | `config/`<br>`app/models/`<br>`app/routes/auth.py` | `app/templates/auth/`<br>`app/templates/layouts/` | Khởi tạo khung dự án, thiết kế CSDL 23 bảng, bảo mật đăng nhập/đăng ký scrypt, phân quyền vai trò, quản lý GitHub và Deploy Cloud. |
| **2** | **Thành viên 2** | `...` | **Client Portal & Booking** | `app/routes/client.py` | `app/templates/client/` | Xây dựng trang chủ, giới thiệu dịch vụ, form đặt lịch hẹn trực tuyến, kiểm tra chống trùng giờ khám (BR-02), quản lý hồ sơ thú cưng. |
| **3** | **Thành viên 3** | `...` | **Doctor Portal & Records** | `app/routes/doctor.py` | `app/templates/doctor/` | Xây dựng hàng đợi khám bệnh trong ngày, màn hình bác sĩ khám lâm sàng, chẩn đoán bệnh án điện tử, chức năng kê đơn thuốc. |
| **4** | **Thành viên 4** | `...` | **Staff Portal & Payment QR** | `app/routes/staff.py` | `app/templates/staff/` | Màn hình tiếp tân check-in bệnh nhân tại quầy, phân buồng khám, xuất hóa đơn viện phí và tích hợp thanh toán quét mã **VietQR Napas 247**. |
| **5** | **Thành viên 5** | `...` | **Pharmacy & Inventory** | `app/routes/pharmacy.py` | `app/templates/pharmacy/` | Quản lý danh mục thuốc và vắc-xin, quản lý nhập kho theo lô/hạn dùng, cảnh báo thuốc sắp hết, tự động trừ kho nguyên tử (BR-08). |
| **6** | **Thành viên 6** | `...` | **Admin Management & Charts** | `app/routes/admin.py` | `app/templates/admin/` | Bảng điều khiển KPI quản trị, vẽ biểu đồ doanh thu Chart.js, thống kê số ca khám, quản trị tài khoản nhân sự và phân quyền. |

👉 *Xem lộ trình chi tiết từng tuần tại:* [docs/phan-cong-nhiem-vu.md](docs/phan-cong-nhiem-vu.md)

---

## 📂 2. CẤU TRÚC THƯ MỤC DỰ ÁN DÀNH CHO 6 THÀNH VIÊN

```text
petcare/
├── app.py                         <-- [TRƯỞNG NHÓM] Điểm khởi động ứng dụng Flask
├── config/                        <-- [TRƯỞNG NHÓM] Cấu hình môi trường (Dev, Test, Prod)
├── requirements.txt               <-- [TRƯỞNG NHÓM] Thư viện Python của dự án
├── Dockerfile & docker-compose    <-- [TRƯỞNG NHÓM] Môi trường Docker container
│
├── database/                      <-- [TRƯỞNG NHÓM] Cơ sở dữ liệu chuẩn
│   ├── schema.sql                 <-- CSDL 23 bảng quan hệ (InnoDB, Khóa ngoại, Ràng buộc)
│   └── seed.sql                   <-- Dữ liệu mẫu ban đầu phòng khám
│
├── app/
│   ├── __init__.py                <-- [TRƯỞNG NHÓM] Application Factory ghép nối 6 phân hệ
│   │
│   ├── routes/                    <-- NƠI 6 THÀNH VIÊN VIẾT CODE LOGIC (Mỗi người 1 file)
│   │   ├── auth.py                <-- [THÀNH VIÊN 1] Đăng nhập, Đăng ký, Đổi mật khẩu
│   │   ├── client.py              <-- [THÀNH VIÊN 2] Trang chủ & Đặt lịch hẹn khám
│   │   ├── doctor.py              <-- [THÀNH VIÊN 3] Khám bệnh & Kê đơn thuốc
│   │   ├── staff.py               <-- [THÀNH VIÊN 4] Tiếp nhận bệnh nhân & VietQR
│   │   ├── pharmacy.py            <-- [THÀNH VIÊN 5] Quản lý Kho thuốc & Vaccine
│   │   ├── admin.py               <-- [THÀNH VIÊN 6] Báo cáo Doanh thu & Quản trị
│   │   └── api/                   <-- RESTful API endpoints dùng chung
│   │
│   ├── templates/                 <-- NƠI 6 THÀNH VIÊN XÂY DỰNG GIAO DIỆN HTML
│   │   ├── layouts/base.html      <-- Khung giao diện dùng chung (Header, Navbar, Footer)
│   │   ├── auth/                  <-- [THÀNH VIÊN 1] login.html, register.html
│   │   ├── client/                <-- [THÀNH VIÊN 2] home.html, booking.html, services.html
│   │   ├── doctor/                <-- [THÀNH VIÊN 3] queue.html, examine.html, prescription.html
│   │   ├── staff/                 <-- [THÀNH VIÊN 4] checkin.html, invoices.html, payment.html
│   │   ├── pharmacy/              <-- [THÀNH VIÊN 5] medicines.html, import.html, alerts.html
│   │   ├── admin/                 <-- [THÀNH VIÊN 6] dashboard.html, users.html, reports.html
│   │   └── errors/                <-- Giao diện bắt lỗi chuẩn 400, 403, 404, 500
│   │
│   └── static/                    <-- Tài nguyên dùng chung
│       ├── css/style.css          <-- Bộ màu nhận diện thương hiệu (#1F7A63 & #F29F3D)
│       └── js/main.js             <-- Xử lý tương tác giao diện JavaScript
│
└── docs/                          <-- TÀI LIỆU DỰ ÁN NỘP GIẢNG VIÊN
    ├── phan-cong-nhiem-vu.md      <-- Kế hoạch & Checklist 6 tuần của nhóm
    └── dac-ta-yeu-cau.md          <-- Đặc tả kỹ thuật & 14 quy tắc nghiệp vụ (BR-01 -> BR-14)
```

---

## 🚀 3. HƯỚNG DẪN CÀI ĐẶT & CHẠY DỰ ÁN TRÊN MÁY CÁ NHÂN

Dành cho cả 6 thành viên khi tải code về máy:

### Bước 1: Sao chép (Clone) dự án về máy
```bash
git clone https://github.com/lenguyennhattruongg/petcare.git
cd petcare
```

### Bước 2: Tạo và kích hoạt môi trường ảo Python
* Trên Windows (PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\activate
```
* Trên macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Bước 3: Cài đặt các thư viện cần thiết
```bash
pip install -r requirements.txt
```

### Bước 4: Khởi tạo biến môi trường
Tạo file `.env` từ file mẫu `.env.example`:
```bash
cp .env.example .env
```

### Bước 5: Chạy ứng dụng
```bash
python app.py
```
Mở trình duyệt truy cập: **`http://localhost:5000`**

---

## 🛠️ 4. QUY TRÌNH NỘP CODE TRÊN GITHUB DÀNH CHO THÀNH VIÊN

Để đảm bảo nhóm làm việc mượt mà, **mỗi thành viên khi code phải tuân thủ 5 bước sau**:

1. **Chuyển sang nhánh phát triển và cập nhật code mới nhất:**
   ```bash
   git checkout dev
   git pull origin dev
   ```
2. **Tạo nhánh riêng mang tên mình:**
   ```bash
   # Ví dụ: Thành viên 2 làm chức năng đặt lịch
   git checkout -b feature/member2-booking
   ```
3. **Viết code trong thư mục của mình và lưu lại (Commit):**
   ```bash
   git add .
   git commit -m "[TV2] Hoan thien giao dien form dat lich kham"
   ```
4. **Đẩy nhánh của mình lên GitHub:**
   ```bash
   git push origin feature/member2-booking
   ```
5. **Tạo Pull Request (PR):**
   * Truy cập [https://github.com/lenguyennhattruongg/petcare](https://github.com/lenguyennhattruongg/petcare)
   * Nhấn **Compare & pull request**, chọn gộp vào nhánh **`dev`**.
   * Báo Trưởng nhóm (Nhật Trường) vào xem và duyệt (**Merge**) vào nhánh chung.

---

## 💡 5. CÔNG NGHỆ ÁP DỤNG

* **Backend:** Python 3.12, Flask 3.0+, Flask-SQLAlchemy (ORM), Flask-Login, Flask-WTF (CSRF Protection), Werkzeug (Scrypt Hashing).
* **Database:** MySQL 8.0+ (InnoDB, UTF8MB4, ACID Transactions).
* **Frontend:** HTML5 Semantic, CSS3 Custom Tokens, JavaScript ES6+, Bootstrap 5.3, Bootstrap Icons, Chart.js.
* **Tích hợp:** Cổng thanh toán quét mã QR động **VietQR (Napas 247)**.
* **DevOps:** Git/GitHub, Docker, Docker-Compose, Cloud Hosting (Render / PythonAnywhere).

---

&copy; 2026 Nhóm 2 - Học phần Lập trình Web - UTH.
