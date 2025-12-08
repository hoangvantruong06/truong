print("Hoang Van Truong\nMSV:245752021610137");
def count_file_stats(filename):
    """Đọc file và tính số ký tự, số từ, số dòng."""
    char_count = 0  # Số ký tự
    word_count = 0  # Số từ
    line_count = 0  # Số dòng

    try:
        # Mở file để đọc ('r')
        with open(filename, 'r') as file:
            for line in file:
                line_count += 1
                
                # Cập nhật số ký tự
                char_count += len(line)
                
                # Cập nhật số từ: tách dòng thành các từ bằng split()
                # và cộng số lượng từ tìm được
                words = line.split()
                word_count += len(words)

        # In kết quả
        print(f"\n--- Thống kê File '{filename}' ---")
        print(f"Tổng số dòng: {line_count}")
        print(f"Tổng số từ: {word_count}")
        print(f"Tổng số ký tự (bao gồm khoảng trắng và ký tự xuống dòng): {char_count}")

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file {filename}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Ví dụ sử dụng:
# Giả sử bạn có file 'D:/a.txt'
count_file_stats('E:/A.txt')
