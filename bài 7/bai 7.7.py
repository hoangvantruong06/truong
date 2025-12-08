print("Hoang Van Truong\nMSV:245752021610137");
def count_lines(fname):
    """Đếm và in ra tổng số dòng của file."""
    try:
        count = 0
        with open(fname, 'r') as f:
            for line in f:
                count += 1
        print(f"\nFile '{fname}' có tổng cộng {count} dòng.")
        return count
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file {fname}")
        return 0

# Ví dụ sử dụng:
count_lines('E:/a.txt')
