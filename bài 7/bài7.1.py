print("Hoang Van Truong\nMSV:245752021610137");
input_file = open('C:/A.txt', 'r')
lines = input_file.readlines()
input_file.close()
print("Nội dung file được in đảo ngược:")
for i in range(len(lines) -1, -1, -1):
    print(lines[i].strip(), end='\n')
