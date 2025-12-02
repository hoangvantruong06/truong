print ("Hoàng Văn Trường\nMSV:245752021610137");
import mymath
import mymath as mt  
values = [2, 4, 6, 8, 10]
print('Squares:')
for v in values:
    print(mymath.square(v))

print('Cubes:')
for v in values:
    print(mt.cube(v))

print('Average: ' + str(mymath.average(values)))
print(f"mt.square(2) = {mt.square(2)}")
print(f"mt.square(3) = {mt.square(3)}")
