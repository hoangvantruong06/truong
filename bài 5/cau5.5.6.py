
input_data = '14,46,43,27,57,41,45,21,70'
data_list = [int(item.strip()) for item in input_data.split(',')]
min_value = min(data_list)
max_value = max(data_list)
min_index = data_list.index(min_value)
max_index = data_list.index(max_value)
print(f"Danh sách: {data_list}")
print(f"Phần tử nhỏ nhất: {min_value} tại vị trí: {min_index}")
print(f"Phần tử lớn nhất: {max_value} tại vị trí: {max_index}")
