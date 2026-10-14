"""
=============================================================================
MODULE: AUTHENTICATION & USER MANAGEMENT (XÁC THỰC & PHÂN QUYỀN)
PHỤ TRÁCH: THÀNH VIÊN 1 - Lê Nguyễn Nhật Trường (Trưởng nhóm / DevOps / Auth)
NHIỆM VỤ:
  - Đăng ký tài khoản khách hàng mới (Khách vãng lai -> Khách hàng thành viên)
  - Đăng nhập hệ thống (Phân luồng tự động: Admin -> /admin, Bác sĩ -> /doctor, Tiếp tân -> /staff, Khách -> /)
  - Đăng xuất & Quản lý phiên làm việc (Session & CSRF Token)
  - Đổi mật khẩu, quên mật khẩu (Mã hóa scrypt bảo mật)
=============================================================================
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    """Trang đăng nhập hệ thống PetCare"""
    if current_user.is_authenticated:
        return redirect(url_for("client.home"))
        
    if request.method == "POST":
        # TODO: Thành viên 1 xử lý xác thực tài khoản tại đây
        flash("Tính năng đăng nhập đang được hoàn thiện.", "info")
        return redirect(url_for("auth.login"))

    return render_template("auth/login.html")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    """Trang đăng ký tài khoản cho khách hàng mới"""
    if current_user.is_authenticated:
        return redirect(url_for("client.home"))

    if request.method == "POST":
        # TODO: Thành viên 1 xử lý lưu khách hàng mới vào Database
        flash("Đăng ký tài khoản thành công! Vui lòng đăng nhập.", "success")
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html")


@auth_bp.route("/logout")
@login_required
def logout():
    """Đăng xuất khỏi hệ thống"""
    logout_user()
    flash("Bạn đã đăng xuất thành công.", "info")
    return redirect(url_for("client.home"))


@auth_bp.route("/profile")
@login_required
def profile():
    """Thông tin cá nhân người dùng hiện tại"""
    return render_template("auth/profile.html")
