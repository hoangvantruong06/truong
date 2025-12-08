print("Hoang Van Truong\nMSV:245752021610137");
class IOString:
    def __init__(self):
        # Thuộc tính lưu trữ chuỗi
        self.str1 = ""

    # Phương thức nhận chuỗi từ người dùng
    def get_String(self):
        # Sử dụng input() để nhận giá trị
        self.str1 = input("Vui lòng nhập một chuỗi: ")

    # Phương thức in chuỗi bằng chữ in hoa
    def print_String(self):
        print(self.str1.upper())

# Kiểm tra
str_io = IOString()
str_io.get_String() # Yêu cầu người dùng nhập
print("Chuỗi in hoa:")
str_io.print_String()
