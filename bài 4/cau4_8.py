print("Hoang Van Truong\nMSV:245752021610137");
day_tu = input('Nhập dãy từ: ').split() # Tách input thành list các từ

if not day_tu:
    print("Không có từ nào được nhập.")
else:
    # Tìm độ dài lớn nhất
    max_length = 0
    for tu in day_tu:
        if len(tu) > max_length:
            max_length = len(tu)
            
    # In ra tất cả các từ có độ dài bằng max_length
    print(f"Các từ có độ dài tối đa ({max_length} ký tự):")
    for tu in day_tu:
        if len(tu) == max_length:
            print(tu)
