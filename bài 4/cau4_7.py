print("Hoang Van Truong\nMSV:245752021610137");
chuoi_goc = input('Nhập chuỗi: ')
chuoi_moi = ''

for char in chuoi_goc:
    # Kiểm tra xem ký tự có phải là chữ số hay không
    if not char.isdigit():
        chuoi_moi += char # Nếu không phải chữ số, thêm vào chuỗi mới

print(f"Chuỗi sau khi loại bỏ số: {chuoi_moi}")
