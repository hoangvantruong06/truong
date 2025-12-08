print("Hoang Van Truong\nMSV:245752021610137");
import tkinter as tk
import random
import time

# --- 1. Thiết lập biến toàn cục và Cấu hình game ---
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'Purple', 'Brown']
score = 0
timeleft = 30 # Thời gian game, ban đầu 30 giây

# Cấu hình cửa sổ chính
root = tk.Tk()
root.title("Color Game")
root.geometry("400x250")

# --- 2. Các hàm chức năng ---

def startGame(event):
    """Bắt đầu trò chơi khi nhấn Enter."""
    global timeleft
    if timeleft == 30: # Chỉ bắt đầu khi game chưa chạy
        # Bắt đầu đếm ngược
        countdown() 
    
    # Bắt đầu vòng chơi
    nextColour()

def nextColour():
    """Chọn và hiển thị màu tiếp theo."""
    global score
    global timeleft
    
    # 1. Nếu game đang chạy
    if timeleft > 0:
        # Làm cho ô nhập liệu hoạt động
        e.focus_set() 
        
        # 2. Kiểm tra nếu màu gõ vào bằng màu của chữ
        # e.get().lower(): lấy chữ người dùng nhập, chuyển về chữ thường.
        # colours[1].lower(): màu CHỮ (màu hiển thị) của từ cuối cùng.
        if e.get().lower() == colours[1].lower():
            score += 1 # Tăng điểm nếu đúng
            
        # 3. Xóa ô nhập liệu
        e.delete(0, tk.END) 
        
        # 4. Xáo trộn danh sách màu (để chọn ngẫu nhiên màu cho từ và màu cho chữ)
        random.shuffle(colours) 
        
        # 5. Thay đổi loại màu (màu chữ và văn bản)
        # text=str(colours[1]): từ được hiển thị (tên màu - tên từ).
        # fg=str(colours[0]): màu của từ được hiển thị (tên màu - màu chữ).
        colourLabel.config(fg = str(colours[0]), text = str(colours[1])) 
        
        # 6. Cập nhật điểm
        scoreLabel.config(text = "Score: " + str(score))

def countdown():
    """Hàm đếm ngược thời gian."""
    global timeleft
    
    if timeleft > 0:
        # Giảm thời gian
        timeleft -= 1
        
        # Cập nhật hiển thị thời gian
        timeLabel.config(text = "Time left: " + str(timeleft)) 
        
        # Gọi lại hàm countdown sau 1 giây
        timeLabel.after(1000, countdown)
    else:
        # Thông báo kết thúc game
        colourLabel.config(fg = "black", text = "Game Over!")
        e.config(state='disabled') # Vô hiệu hóa ô nhập liệu khi hết giờ


# --- 3. Tạo các Widget ---

# Nhãn hiển thị điểm
scoreLabel = tk.Label(root, text = "Score: " + str(score), font = ('Helvetica', 12))
scoreLabel.pack(pady=10)

# Nhãn hiển thị thời gian
timeLabel = tk.Label(root, text = "Time left: " + str(timeleft), font = ('Helvetica', 12))
timeLabel.pack(pady=5)

# Nhãn hiển thị từ màu
# Ban đầu hiển thị màu ĐEN, chữ là "Start"
colourLabel = tk.Label(root, font = ('Helvetica', 60), fg="black", text="Start")
colourLabel.pack()

# Ô nhập liệu
e = tk.Entry(root, font = ('Helvetica', 18), justify='center')
# Gắn sự kiện: khi nhấn phím Enter, gọi hàm startGame
root.bind('<Return>', startGame) 
e.pack(pady=10)

# Cung cấp focus cho ô nhập liệu khi khởi động
e.focus_set() 

# --- 4. Mainloop ---
root.mainloop()
