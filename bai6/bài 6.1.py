print("Hoang Van Truong\nMSV:245752021610137");
class Circle:
    # Phương thức khởi tạo
    def __init__(self, r):
        self.radius = r
    
    # Phương thức tính diện tích (Area)
    def area(self):
        # Sử dụng giá trị xấp xỉ của Pi là 3.14
        return self.radius**2 * 3.14

# Kiểm tra
aCircle = Circle(2)
print(f"Bán kính: {aCircle.radius}")
print(f"Diện tích của Circle(2): {aCircle.area()}")
