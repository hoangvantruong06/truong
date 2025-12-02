print ("Hoàng Văn Trường\nMSV:245752021610137");
str=input("enter a string:")
dict ={}
for n in str:
    keys = dict.keys()
    if n in keys:
        dict[n] += 1
    else:
        dict[n] =1
print (dict)
