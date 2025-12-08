print("Hoang Van Truong\nMSV:245752021610137");
import os

def file_read_from_tail(fname, lines):
    """Đọc và in ra n dòng cuối cùng của file."""
    try:
        # Cách đơn giản và phổ biến nhất: đọc hết file vào list
        with open(fname, 'r') as f:
            all_lines = f.readlines()
        
        # Dùng slicing để lấy n dòng cuối cùng (từ vị trí -lines trở đi)
        last_n_lines = all_lines[-lines:]
        
        print(f"\n--- {lines} dòng cuối cùng của file '{fname}' ---")
        for line in last_n_lines:
            print(line.strip())
            
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file {fname}")
    
# Ví dụ sử dụng:
# Giả sử file 'test.txt' có ít nhất 2 dòng
file_read_from_tail('E:/a.txt', 2)
