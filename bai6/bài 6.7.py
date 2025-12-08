print("Hoang Van Truong\nMSV:245752021610137");
class Circle:
    # Phương thức khởi tạo
    def __init__(self, r):
        self.radius = r
        self.PI = 3.14159

    # Phương thức tính diện tích (Area)
    def tinh_dientich(self):
        return self.PI * self.radius**2
    
    # Phương thức tính chu vi (Circumference)
    def tinh_chuvi(self):
        return 2 * self.PI * self.radius

# Kiểm tra
c1 = Circle(5)
print(f"Circle bán kính 5:")
print(f"Diện tích: {c1.tinh_dientich():.2f}")
print(f"Chu vi: {c1.tinh_chuvi():.2f}")
