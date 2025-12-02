print("Hoang Van Truong\nMSV:245752021610137");
ten_day_du = input('Nhập họ và tên (ví dụ: Nguyen Van An): ')
# Tách chuỗi thành list các từ
parts = ten_day_du.split()

# Họ là phần tử đầu tiên
ho = parts[0]

# Tên riêng là phần tử cuối cùng
ten_rieng = parts[-1] 

# Tên đệm là các phần tử ở giữa (nếu có)
ten_dem = " ".join(parts[1:-1])

print(f"Họ: {ho}")
print(f"Tên đệm: {ten_dem}")
print(f"Tên riêng: {ten_rieng}")

# Theo giả thiết đơn giản (chỉ cần Họ và Tên riêng một âm):
# print(f"Họ: {ho}")
# print(f"Tên riêng: {ten_rieng}")
