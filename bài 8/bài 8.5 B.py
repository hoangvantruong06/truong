print("Hoang Van Truong\nMSV:245752021610137");
import tkinter as tk

def ShowChoice():
    print(v.get())

root = tk.Tk()
root.title("tk")

v = tk.IntVar()
v.set(1) 

languages = [
    ("Python 1", 1), # Thay đổi nhãn để phù hợp với hình ảnh
    ("Perl 2", 2),
    ("Java 3", 3),
    ("C++ 4", 4),
    ("C# 5", 5)
]

# Thêm Label
tk.Label(root, 
         text="""Choose your favourite 
programming language:""",
         justify = tk.LEFT,
         padx = 20).pack(anchor=tk.W)

# Tạo và đóng gói các Radiobutton với indicatoron=0
for text, val in languages:
    tk.Radiobutton(root, 
                   text=text,
                   padx = 20, 
                   indicatoron = 0, # <-- Thay đổi thành indicator
                   width = 20, # Thiết lập chiều rộng để các nút đều nhau
                   variable=v, 
                   command=ShowChoice,
                   value=val).pack(anchor=tk.W)

root.mainloop()
