print("Hoang Van Truong\nMSV:245752021610137");
import tkinter as tk

# Xây dựng cửa sổ form
window = tk.Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200') # Thiết lập kích thước cửa sổ

# Thêm widget Label
lbl = tk.Label(window, text="Hello")
lbl.grid(column=0, row=0) # Đặt Label tại cột 0, hàng 0

# Thêm widget Button
btn = tk.Button(window, text="Click Me", command=clicked) # Command sẽ được định nghĩa sau
btn.grid(column=1, row=0) # Đặt Button tại cột 1, hàng 0
