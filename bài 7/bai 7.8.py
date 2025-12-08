print("Hoang Van Truong\nMSV:245752021610137");
def write_list_to_file(fname, data_list):
    """Ghi nội dung của một list vào file."""
    try:
        # Mở file ở chế độ 'w' (ghi đè) hoặc 'a' (nối thêm)
        with open(fname, 'w', encoding='utf-8') as f:
            for item in data_list:
                # Ghi từng phần tử và thêm ký tự xuống dòng '\n'
                f.write(str(item) + '\n') 
        print(f"\nĐã ghi {len(data_list)} mục vào file '{fname}' thành công.")
    except Exception as e:
        print(f"Đã xảy ra lỗi khi ghi file: {e}")

# Ví dụ sử dụng:
data = ["Dòng 1: Hello Python", "Dòng 2: File Handling", "Dòng 3: Bài tập 8"]
write_list_to_file('E:/a.txt', data)
    
