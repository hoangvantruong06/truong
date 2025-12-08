print("Hoang Van Truong\nMSV:245752021610137");
class Hinhchunhat:
    # Phương thức khởi tạo
    def __init__(self, chieudai, chieurong):
        self.dai = chieudai
        self.rong = chieurong
        
    # Phương thức tính diện tích (Area)
    def area(self):
        return self.dai * self.rong

# Kiểm tra
hcn1 = Hinhchunhat(10, 5)
print(f"Hình chữ nhật có chiều dài 10, rộng 5. Diện tích: {hcn1.area()}")
