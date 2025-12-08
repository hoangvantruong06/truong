print("Hoang Van Truong\nMSV:245752021610137");
class Nguoi(object):
    # Phương thức cơ sở, trả về giá trị mặc định
    def getGender(self):
        return "Unknown"

class Nam(Nguoi):
    # Ghi đè (Override) phương thức getGender
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    # Ghi đè (Override) phương thức getGender
    def getGender(self):
        return "Nu"

# Kiểm tra
aNam = Nam()
aNu = Nu()
aNguoi = Nguoi()

print(f"Đối tượng Nam: {aNam.getGender()}")
print(f"Đối tượng Nữ: {aNu.getGender()}")
print(f"Đối tượng Nguoi: {aNguoi.getGender()}")
