print("Hoang Van Truong\nMSV:245752021610137");
import tkinter as tk

# Các hàm xử lý lệnh
def NewFile():
    print("New File!")

def OpenFile():
    print("Open File!")

def ExitApp():
    root.quit() # Thoát ứng dụng

def About():
    print("This is a simple example of a menu")

# Bổ sung các hàm cho Insert (Bước 3)
def InsText():
    print("Insert Text!")

def InsPic():
    print("Insert Picture!")

root = tk.Tk()
root.title("tk") # Tên cửa sổ

# Tạo Menu chính
menu = tk.Menu(root)
root.config(menu=menu) # Gán menu vào cửa sổ

# 1. Tạo menu "File"
filemenu = tk.Menu(menu, tearoff=0) # tearoff=0 loại bỏ gạch ngang (dùng để tách menu)
menu.add_cascade(label="File", menu=filemenu) 
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile) # Thêm Open
filemenu.add_separator() # Dòng ngăn cách
filemenu.add_command(label="Exit", command=ExitApp) # Sử dụng hàm ExitApp

# 2. Tạo menu "Insert" (Theo yêu cầu Hình B2)
insertmenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Insert", menu=insertmenu)
insertmenu.add_command(label="Text", command=InsText)
insertmenu.add_command(label="Picture", command=InsPic)

# 3. Tạo menu "Help"
helpmenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=About)

root.mainloop()
