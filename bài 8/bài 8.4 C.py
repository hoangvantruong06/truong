print("Hoang Van Truong\nMSV:245752021610137");
import tkinter as tk

def clicked():
    """Phương thức xử lý sự kiện khi nút được nhấn."""
    # Thay đổi nội dung của Label
    lbl.configure(text="Button was clicked !!")

# Xây dựng cửa sổ form
window = tk.Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

# Thêm widget Label
lbl = tk.Label(window, text="Hello")
lbl.grid(column=0, row=0)

# Thêm widget Button
btn = tk.Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)

window.mainloop()
