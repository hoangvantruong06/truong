print("Hoang Van Truong\nMSV:245752021610137");
# Ví dụ nhập: mot hai ba
ds = input('Nhập chuỗi từ: ').split() 
# ds sẽ là ['mot', 'hai', 'ba']

# Đảo ngược danh sách tại chỗ
ds.reverse()
# ds sau khi đảo ngược là ['ba', 'hai', 'mot']

# Nối các từ lại với nhau bằng khoảng trắng
ket_qua = ' '.join(ds)
print(ket_qua) # Output: ba hai mot

# Hoặc dùng slicing:
# ket_qua = ' '.join(ds[::-1])
