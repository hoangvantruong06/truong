print("Hoang Van Truong\nMSV:245752021610137");
import tkinter as tk

def clicked():
    lbl.configure(text="Button was clicked !!")

window = tk.Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

lbl = tk.Label(window, text="Hello")
lbl.grid(column=0, row=0)

# Thêm Button với màu nền vàng (yellow) và màu chữ đỏ (red)
btn = tk.Button(window, 
                text="Click Me", 
                command=clicked, 
                bg="yellow", 
                fg="red") # <-- Thêm bg và fg
btn.grid(column=1, row=0)

window.mainloop()
