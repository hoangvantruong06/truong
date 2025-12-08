print ("Hoàng Văn Trường\nMSV:245752021610137");
import numpy as np

data_type = [('name', 'S5'), ('class', int), ('height', float)]
students_details = [
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.1),
    ('Pit', 5, 40.11)
]
students = np.array(students_details, dtype=data_type)

print("Dữ liệu đầu vào:", students)

# Sắp xếp theo nhiều cột: ('class', 'height')
# Sắp xếp theo 'class' trước, sau đó là 'height'
students_sorted_multi = np.sort(students, order=('class', 'height'))

print("\nKết quả sắp xếp (Class -> Height):")
print(students_sorted_multi)
# Expected: [('Pit', 5, 40.11) ('Paul', 5, 42.1) ('James', 5, 48.5) ('Nail', 6, 52.5)]
