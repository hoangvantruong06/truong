print("Hoang Van Truong\nMSV:245752021610137");
# Hàm split() mặc định tách chuỗi dựa trên khoảng trắng/tab và trả về một list
ds = input('Danh sách: ').split() 

print("In cả dãy vừa nhập:", ds)

print("In dãy vừa nhập, mỗi phần tử trên một dòng:")
for so in ds:
    print(so)
