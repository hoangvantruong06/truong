print("Hoang Van Truong\nMSV:245752021610137");
import tkinter as tk
from tkinter import messagebox

# Hàm xử lý khi nhấn nút "Click Me"
def show_radio_selection():
    # Lấy giá trị hiện tại của Radiobutton đã chọn
    # Giá trị này tương ứng với value được gán: 1, 2, hoặc 3
    selected_value = radio_var.get()

    # Tạo chuỗi thông tin cá nhân từ các ô nhập liệu
    ho_ten = entry_ho_ten.get()
    ngay_sinh = entry_ngay_sinh.get()
    mssv = entry_mssv.get()
    nganh_hoc = entry_nganh_hoc.get()
    
    # Hiển thị thông tin
    info_message = f"Thông tin cá nhân:\n" \
                   f"Họ tên: {ho_ten}\n" \
                   f"Ngày sinh: {ngay_sinh}\n" \
                   f"MSSV: {mssv}\n" \
                   f"Ngành học: {nganh_hoc}\n" \
                   f"\n" \
                   f"Radio button đã chọn: {selected_value}"
    
    messagebox.showinfo("Kết Quả Lựa Chọn", info_message)

# 1. Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("Chương Trình Thông Tin và Radio Button")

# 2. Xây dựng Form hiển thị thông tin cá nhân (phần a)
## Tạo Frame để nhóm các widgets nhập liệu
info_frame = tk.LabelFrame(root, text="Thông Tin Cá Nhân", padx=10, pady=10)
info_frame.pack(padx=20, pady=10, fill="x")

# Hàng 1: Họ tên
tk.Label(info_frame, text="Họ tên:").grid(row=0, column=0, sticky="w", pady=2)
entry_ho_ten = tk.Entry(info_frame, width=40)
entry_ho_ten.grid(row=0, column=1, padx=5, pady=2)

# Hàng 2: Ngày tháng năm sinh
tk.Label(info_frame, text="Ngày sinh (dd/mm/yyyy):").grid(row=1, column=0, sticky="w", pady=2)
entry_ngay_sinh = tk.Entry(info_frame, width=40)
entry_ngay_sinh.grid(row=1, column=1, padx=5, pady=2)

# Hàng 3: MSSV
tk.Label(info_frame, text="MSSV:").grid(row=2, column=0, sticky="w", pady=2)
entry_mssv = tk.Entry(info_frame, width=40)
entry_mssv.grid(row=2, column=1, padx=5, pady=2)

# Hàng 4: Ngành học
tk.Label(info_frame, text="Ngành học:").grid(row=3, column=0, sticky="w", pady=2)
entry_nganh_hoc = tk.Entry(info_frame, width=40)
entry_nganh_hoc.grid(row=3, column=1, padx=5, pady=2)

# 3. Xây dựng Form có nội dung Radiobutton (phần b)
## Tạo Frame để nhóm các widgets Radiobutton và Button
radio_frame = tk.LabelFrame(root, text="Welcome", padx=10, pady=10)
radio_frame.pack(padx=20, pady=10, fill="x")

# Biến Tkinter để lưu trữ giá trị của Radiobutton đã chọn
# IntVar được dùng vì giá trị mong muốn là số (1, 2, 3)
radio_var = tk.IntVar()
# Thiết lập giá trị mặc định là 1 (First)
radio_var.set(1)

# Tạo các Radiobutton
rb_first = tk.Radiobutton(radio_frame, text="First", variable=radio_var, value=1)
rb_second = tk.Radiobutton(radio_frame, text="Second", variable=radio_var, value=2)
rb_third = tk.Radiobutton(radio_frame, text="Third", variable=radio_var, value=3)

# Đặt các Radiobutton trên cùng một hàng
rb_first.pack(side="left", padx=5)
rb_second.pack(side="left", padx=5)
rb_third.pack(side="left", padx=5)

# Tạo nút "Click Me"
click_me_button = tk.Button(radio_frame, text="Click Me", command=show_radio_selection)
click_me_button.pack(side="left", padx=(15, 0)) # Thêm padding bên trái để căn chỉnh

# Chạy vòng lặp sự kiện chính của Tkinter
root.mainloop()
