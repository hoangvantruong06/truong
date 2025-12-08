print("Hoang Van Truong\nMSV:245752021610137");
def binary_search(item_list, item):
    """Tìm kiếm nhị phân (yêu cầu item_list phải được sắp xếp)."""
    first = 0
    last = len(item_list) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        
        if item_list[mid] == item:
            found = True
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    
    return found

# Sử dụng:
sorted_list = [1, 2, 3, 5, 8]
print(f"Binary_search cho 6: {binary_search(sorted_list, 6)}")
print(f"Binary_search cho 5: {binary_search(sorted_list, 5)}")
