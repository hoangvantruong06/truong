print("Hoang Van Truong\nMSV:245752021610137");
def find_longest_words(fname):
    """Tìm và in ra (các) từ dài nhất trong file."""
    longest_word = ''
    max_length = 0
    longest_words_list = []

    try:
        with open(fname, 'r') as f:
            for line in f:
                # Tách dòng thành các từ. Ký tự xuống dòng, dấu câu cần được xử lý
                # Ta sẽ dùng regex hoặc đơn giản là thay thế một số ký tự đặc biệt
                cleaned_line = line.replace('\n', ' ').replace(',', ' ').replace('.', ' ')
                words = cleaned_line.split()
                
                for word in words:
                    # Loại bỏ khoảng trắng/ký tự thừa ở đầu/cuối từ
                    word = word.strip() 
                    if len(word) > max_length:
                        max_length = len(word)
                        longest_words_list = [word] # Bắt đầu danh sách mới
                    elif len(word) == max_length and word not in longest_words_list:
                        longest_words_list.append(word) # Thêm từ cùng độ dài

        if max_length > 0:
            print(f"\nTừ (các từ) dài nhất trong file '{fname}' có độ dài {max_length}:")
            for word in longest_words_list:
                print(f"- **{word}**")
        else:
            print(f"File '{fname}' không có từ nào.")

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file {fname}")

# Ví dụ sử dụng:
find_longest_words('E:/A.txt')
