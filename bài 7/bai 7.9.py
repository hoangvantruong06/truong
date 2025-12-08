print("Hoang Van Truong\nMSV:245752021610137");
def copy_file(source_fname, destination_fname):
    """Sao chép toàn bộ nội dung từ file nguồn sang file đích."""
    try:
        # Mở file nguồn để đọc ('r') và file đích để ghi ('w')
        with open(source_fname, 'r') as source, open(destination_fname, 'w') as destination:
            # Đọc toàn bộ nội dung file nguồn
            content = source.read()
            # Ghi nội dung đó vào file đích
            destination.write(content)
            
        print(f"\nĐã sao chép nội dung từ '{source_fname}' sang '{destination_fname}' thành công.")
        
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file nguồn hoặc file đích.")
    except Exception as e:
        print(f"Đã xảy ra lỗi sao chép: {e}")

# Ví dụ sử dụng:
copy_file('E:/b.txt', 'b_copy.txt')
