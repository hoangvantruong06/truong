print("Hoang Van Truong\nMSV:245752021610137");
import turtle

# Thiết lập cửa sổ
window = turtle.Screen()
window.bgcolor("lightgreen")

# Tạo đối tượng rùa (painter)
painter = turtle.Turtle()
painter.color('blue') # Màu nét vẽ
painter.pensize(3)    # Độ dày nét vẽ
# painter.fillcolor('blue') # Dòng này có thể không cần thiết nếu không tô màu

def drawsq(t, s):
    """Hàm vẽ hình vuông có độ dài cạnh s"""
    for i in range(4):
        t.forward(s)
        t.left(90)

# Thực hiện vòng lặp vẽ và xoay hình vuông
# Vòng lặp này sẽ xoay 180 lần, mỗi lần xoay 2 độ (180 * 2 = 360 độ)
for i in range(1, 180):
    painter.left(2) # Xoay rùa 2 độ
    drawsq(painter, 200) # Vẽ hình vuông cạnh 200
    
# Thêm dòng này để cửa sổ không đóng ngay lập tức
window.mainloop()
