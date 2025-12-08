print ("Hoàng Văn Trường\nMSV:245752021610137");
import datetime as dt

format_str = '%Y-%m-%dT%H:%M:%S'
t1 = dt.datetime.strptime('2008-10-12T14:45:52', format_str)

print(f"Day: {t1.day}")
print(f"Month: {t1.month}")
print(f"Minute: {t1.minute}")
print(f"Second: {t1.second}")

t2 = dt.datetime.now()
diff = t2 - t1
print(f"How many days difference? {diff.days}")
