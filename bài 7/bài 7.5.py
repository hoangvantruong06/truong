print("Hoang Van Truong\nMSV:245752021610137");
from itertools import islice

def file_read(fname):
    """Ghi nội dung vào file và sau đó đọc, hiển thị nội dung đó."""
    
    # Ghi nội dung vào file (chế độ 'w' - ghi đè)
    with open(fname, "w") as myfile:
        myfile.write("Python Exercises\n")
        myfile.write("Java Exercises\n")
        
    # Đọc và hiển thị nội dung vừa ghi
    try:
        with open(fname, 'r') as txt:
            print(f"\n--- Nội dung file '{fname}' sau khi ghi ---")
            print(txt.read())
            
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file {fname}")

# Ví dụ sử dụng:
file_read('A.txt')
