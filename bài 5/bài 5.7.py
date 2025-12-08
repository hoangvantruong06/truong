print("Hoang Van Truong\nMSV:245752021610137");
import numpy as np

data_type = [('name', 'S5'), ('class', int), ('height', float)]

students_details = [
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.1),
    ('Pit', 5, 40.11)
]
students = np.array(students_details, dtype=data_type)

print("Original Array:")
print(students)

students_sorted = np.sort(students, order='height')

print("\nSort by height:")
print(students_sorted)
