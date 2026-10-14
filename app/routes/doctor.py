"""
=============================================================================
MODULE: DOCTOR PORTAL (CỔNG BÁC SĨ THÚ Y)
PHỤ TRÁCH: THÀNH VIÊN 3
NHIỆM VỤ:
  - Xem danh sách ca khám trong ngày theo phòng khám (Hàng đợi khám bệnh)
  - Màn hình khám bệnh: Ghi nhận cân nặng, triệu chứng, chẩn đoán (ICD-Vet)
  - Kê đơn thuốc điện tử (chọn thuốc, liều dùng, số ngày sử dụng)
  - Xem lại lịch sử các lần khám trước của thú cưng
=============================================================================
"""
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required

doctor_bp = Blueprint("doctor", __name__, url_prefix="/doctor")


@doctor_bp.route("/")
@doctor_bp.route("/queue")
@login_required
def queue():
    """Hàng đợi khám bệnh trong ngày của bác sĩ"""
    # TODO: Thành viên 3 lấy danh sách ca khám có trạng thái CHECKED_IN
    appointments = []
    return render_template("doctor/queue.html", appointments=appointments)


@doctor_bp.route("/examine/<int:appointment_id>", methods=["GET", "POST"])
@login_required
def examine(appointment_id):
    """Màn hình khám bệnh & chẩn đoán bệnh án"""
    if request.method == "POST":
        # TODO: Thành viên 3 lưu chẩn đoán vào bảng medical_records
        flash("Lưu hồ sơ bệnh án thành công!", "success")
        return redirect(url_for("doctor.prescription", appointment_id=appointment_id))
    return render_template("doctor/examine.html", appointment_id=appointment_id)


@doctor_bp.route("/prescription/<int:appointment_id>", methods=["GET", "POST"])
@login_required
def prescription(appointment_id):
    """Màn hình kê đơn thuốc điện tử"""
    if request.method == "POST":
        # TODO: Thành viên 3 lưu đơn thuốc vào bảng prescriptions & prescription_items
        flash("Đã hoàn tất kê đơn thuốc cho thú cưng!", "success")
        return redirect(url_for("doctor.queue"))
    return render_template("doctor/prescription.html", appointment_id=appointment_id)
