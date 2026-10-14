"""
=============================================================================
MODULE: CLIENT PORTAL (CỔNG THÔNG TIN KHÁCH HÀNG & ĐẶT LỊCH)
PHỤ TRÁCH: THÀNH VIÊN 2
NHIỆM VỤ:
  - Trang chủ giới thiệu phòng khám, danh mục dịch vụ, bảng giá
  - Trang đặt lịch khám trực tuyến (chọn thú cưng, chọn bác sĩ, chọn khung giờ)
  - Kiểm tra và ngăn chặn đặt trùng slot khám (BR-02)
  - Quản lý hồ sơ thú cưng và tra cứu lịch sử khám bệnh của chủ nuôi
=============================================================================
"""
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user

client_bp = Blueprint("client", __name__)


@client_bp.route("/")
def home():
    """Trang chủ cổng thông tin Trung tâm Thú y PetCare"""
    featured_services = [
        {
            "id": 1,
            "name": "Khám Sức Khỏe Tổng Quát",
            "description": "Kiểm tra toàn diện tim mạch, hô hấp, mắt, răng miệng và thể trạng của bé cưng.",
            "price": "150.000₫",
            "duration": "30 phút",
            "icon": "bi-heart-pulse",
        },
        {
            "id": 2,
            "name": "Tiêm Phòng Vắc-xin Đa Giá",
            "description": "Tiêm phòng 7 bệnh cho chó, 4 bệnh cho mèo và vắc-xin dại nhập khẩu chính hãng.",
            "price": "250.000₫",
            "duration": "30 phút",
            "icon": "bi-shield-check",
        },
        {
            "id": 3,
            "name": "Spa & Grooming Chuyên Nghiệp",
            "description": "Tắm sấy dưỡng lông, cắt tỉa thẩm mỹ, vệ sinh tai móng với tinh dầu thư giãn.",
            "price": "300.000₫",
            "duration": "60 phút",
            "icon": "bi-scissors",
        },
        {
            "id": 4,
            "name": "Phẫu Thuật & Triệt Sản An Toàn",
            "description": "Phòng mổ vô trùng áp lực dương, gây mê khí dung hiện đại, chăm sóc hậu phẫu chu đáo.",
            "price": "800.000₫",
            "duration": "60 phút",
            "icon": "bi-bandaid",
        },
    ]
    return render_template("client/home.html", services=featured_services)


@client_bp.route("/services")
def services():
    """Trang danh mục bảng giá dịch vụ"""
    return render_template("client/services.html")


@client_bp.route("/booking", methods=["GET", "POST"])
def booking():
    """Đặt lịch khám bệnh trực tuyến"""
    if request.method == "POST":
        # TODO: Thành viên 2 xử lý đặt lịch và kiểm tra trùng lịch (BR-02)
        flash("Lịch hẹn của bạn đã được tiếp nhận!", "success")
        return redirect(url_for("client.home"))
    return render_template("client/booking.html")


@client_bp.route("/my-pets")
@login_required
def my_pets():
    """Quản lý danh sách thú cưng của khách hàng"""
    return render_template("client/my-pets.html")
