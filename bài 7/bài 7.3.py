print("Hoang Van Truong\nMSV:245752021610137");
# Tên tệp giả định
file_name = 'test.txt' 

def read_full_file(fname):
    """Đọc toàn bộ nội dung của tệp có tên là fname."""
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
            print("--- Nội dung toàn bộ tệp ---")
            print(content)
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy tệp {fname}")
    except Exception as e:
        print(f"Lỗi xảy ra: {e}")

# Ví dụ sử dụng:
# Giả sử tệp 'test.txt' đã tồn tại
# Nếu chưa có, bạn nên tạo nó hoặc sử dụng 'abc.txt' từ Bài 5
read_full_file(file_name)
