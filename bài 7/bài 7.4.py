print("Hoang Van Truong\nMSV:245752021610137");
from itertools import islice

def file_read_from_head(fname, nlines):
    """Đọc và in ra n dòng đầu tiên của file."""
    try:
        with open(fname) as f:
            # islice(iterable, stop) tạo một iterator chỉ lấy các phần tử 
            # từ đầu đến vị trí 'stop' (là nlines)
            print(f"\n--- {nlines} dòng đầu tiên của file '{fname}' ---")
            for line in islice(f, nlines):
                print(line.strip()) # strip() loại bỏ khoảng trắng/xuống dòng thừa
                
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file {fname}")

# Ví dụ sử dụng:
file_read_from_head('E:/a.txt', 4)
