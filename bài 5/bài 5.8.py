print("Hoang Van Truong\nMSV:245752021610137");
def Sequential_Search(dlist, item):
    """Tìm kiếm tuần tự. Trả về (True, index) hoặc (False, -1)."""
    pos = 0
    found = False
    
    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos = pos + 1
            
    if found:
        return (True, pos)
    else:
        return (False, -1)

# Sử dụng:
data_list = [11, 23, 58, 31, 56, 77, 43, 12, 65, 19, 31]
result = Sequential_Search(data_list, 31)
print(f"Sequential_Search cho 31: {result}")
