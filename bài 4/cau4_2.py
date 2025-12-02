print("Hoang Van Truong\nMSV:245752021610137");
S = input('Nhập chuỗi: ')
for ch in S:
    # Nếu không phải là khoảng trắng/tab, thì in ra
    if not ch.isspace():
        print(ch)
