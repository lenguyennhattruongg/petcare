"""
=============================================================================
MODULE: PHARMACY & INVENTORY (QUẢN LÝ NHÀ THUỐC & TỒN KHO)
PHỤ TRÁCH: THÀNH VIÊN 5
NHIỆM VỤ:
  - Quản lý danh mục thuốc thú y, vaccine, vật tư y tế
  - Nhập kho, xuất kho, theo dõi số lượng tồn kho theo lô và hạn sử dụng
  - Cảnh báo thuốc sắp hết hàng (Low Stock Alert)
  - Khấu trừ tồn kho nguyên tử khi đơn thuốc được thanh toán (BR-08)
=============================================================================
"""
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required

pharmacy_bp = Blueprint("pharmacy", __name__, url_prefix="/pharmacy")


@pharmacy_bp.route("/")
@login_required
def index():
    """Trang chủ quản lý kho thuốc"""
    # TODO: Thành viên 5 lấy danh sách thuốc từ bảng medicines
    medicines = []
    return render_template("pharmacy/medicines.html", medicines=medicines)


@pharmacy_bp.route("/import", methods=["GET", "POST"])
def import_stock():
    """Nhập thuốc vào kho"""
    if request.method == "POST":
        # TODO: Thành viên 5 xử lý nhập kho vào bảng inventory_batches
        flash("Nhập kho thành công!", "success")
        return redirect(url_for("pharmacy.index"))
    return render_template("pharmacy/import.html")


@pharmacy_bp.route("/alerts")
@login_required
def stock_alerts():
    """Danh sách thuốc sắp hết hạn hoặc dưới mức tồn kho tối thiểu"""
    # TODO: Thành viên 5 lọc thuốc có quantity <= min_stock
    return render_template("pharmacy/alerts.html")
