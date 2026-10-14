"""
=============================================================================
MODULE: STAFF PORTAL (CỔNG TIẾP TÂN & THU NGÂN)
PHỤ TRÁCH: THÀNH VIÊN 4
NHIỆM VỤ:
  - Tiếp nhận khách hàng & thú cưng đến quầy (Check-in vào hàng đợi)
  - Phân luồng thú cưng vào các phòng khám / bác sĩ đang trực
  - Tạo hóa đơn dịch vụ & thuốc (In phiếu thanh toán)
  - Tích hợp thanh toán quét mã QR động VietQR (Napas 247) tự sinh mã
=============================================================================
"""
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required

staff_bp = Blueprint("staff", __name__, url_prefix="/staff")


@staff_bp.route("/")
@staff_bp.route("/checkin", methods=["GET", "POST"])
@login_required
def checkin():
    """Màn hình tiếp nhận thú cưng tại quầy lễ tân"""
    if request.method == "POST":
        # TODO: Thành viên 4 đổi trạng thái lịch hẹn sang CHECKED_IN
        flash("Tiếp nhận bệnh nhân thành công! Đã chuyển vào phòng khám.", "success")
        return redirect(url_for("staff.checkin"))
    return render_template("staff/checkin.html")


@staff_bp.route("/invoices")
@login_required
def invoices():
    """Danh sách hóa đơn chờ thanh toán trong ngày"""
    # TODO: Thành viên 4 lấy danh sách hóa đơn từ bảng invoices
    invoices = []
    return render_template("staff/invoices.html", invoices=invoices)


@staff_bp.route("/payment/<int:invoice_id>", methods=["GET", "POST"])
@login_required
def payment(invoice_id):
    """Màn hình thanh toán hóa đơn & Tạo mã VietQR động"""
    if request.method == "POST":
        # TODO: Thành viên 4 xác nhận thanh toán hoàn tất (PAID)
        flash("Hóa đơn đã được thanh toán thành công!", "success")
        return redirect(url_for("staff.invoices"))
    return render_template("staff/payment.html", invoice_id=invoice_id)
