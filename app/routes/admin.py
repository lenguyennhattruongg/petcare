"""
=============================================================================
MODULE: ADMIN & ANALYTICS (QUẢN TRỊ VIÊN & THỐNG KÊ DOANH THU)
PHỤ TRÁCH: THÀNH VIÊN 6
NHIỆM VỤ:
  - Dashboard tổng quan số liệu phòng khám theo ngày, tuần, tháng
  - Biểu đồ trực quan doanh thu, số ca khám, dịch vụ phổ biến (Chart.js)
  - Quản lý tài khoản nhân sự (Bác sĩ, Tiếp tân, Quản trị)
  - Quản lý danh mục chủng loại thú cưng, giống loài (Breeds, Species)
=============================================================================
"""
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


@admin_bp.route("/")
@admin_bp.route("/dashboard")
@login_required
def dashboard():
    """Bảng điều khiển trung tâm & Thống kê số liệu"""
    stats = {
        "today_appointments": 12,
        "completed_cases": 8,
        "today_revenue": "4.250.000₫",
        "low_stock_medicines": 3,
    }
    return render_template("admin/dashboard.html", stats=stats)


@admin_bp.route("/users")
@login_required
def users():
    """Quản lý danh sách nhân sự phòng khám"""
    # TODO: Thành viên 6 lấy danh sách nhân viên từ bảng users
    return render_template("admin/users.html")


@admin_bp.route("/reports")
@login_required
def reports():
    """Báo cáo chi tiết doanh thu & bệnh án"""
    return render_template("admin/reports.html")
