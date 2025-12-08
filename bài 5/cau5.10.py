print ("Hoàng Văn Trường\nMSV:245752021610137");
def bubbleSort(nlist):
    """Sắp xếp nổi bọt trên nlist."""
    for passnum in range(len(nlist) - 1, 0, -1): 
        swapped = False
        for i in range(passnum):
            if nlist[i] > nlist[i+1]:
                # Trao đổi
                nlist[i], nlist[i+1] = nlist[i+1], nlist[i]
                swapped = True
        if not swapped:
            break
    return nlist

# Sử dụng:
data_list = [14, 46, 43, 27, 57, 41, 45, 21, 70]
sorted_list = bubbleSort(data_list)
print(f"Dữ liệu sắp xếp (Bubble Sort): {sorted_list}")
