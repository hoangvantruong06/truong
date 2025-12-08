print("Hoang Van Truong\nMSV:245752021610137");
import tkinter as tk

def ShowChoice():
    """In ra giá trị của lựa chọn đã chọn (v.get())."""
    print(v.get())

root = tk.Tk()
root.title("tk")

v = tk.IntVar()
v.set(1) # Khởi tạo lựa chọn mặc định là 1 (Python)

languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C#", 5)
]

# Thêm Label
tk.Label(root, 
         text="""Choose your favourite 
programming language:""",
         justify = tk.LEFT,
         padx = 20).pack(anchor=tk.W) # anchor=tk.W căn lề trái

# Tạo và đóng gói các Radiobutton
for text, val in languages:
    tk.Radiobutton(root, 
                   text=text,
                   padx = 20, 
                   variable=v, # Cùng một biến
                   command=ShowChoice,
                   value=val).pack(anchor=tk.W) # anchor=tk.W căn lề trái

root.mainloop()
