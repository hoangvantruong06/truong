print("Hoang Van Truong\nMSV:245752021610137");
class RomanConverter:
    def roman_to_int(self, s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        
        # Duyệt chuỗi từ trái sang phải
        for i in range(len(s)):
            current_value = rom_val[s[i]]
            
            # Kiểm tra nếu ký tự hiện tại (s[i]) nhỏ hơn ký tự tiếp theo (s[i+1])
            # (Ví dụ: 'IV' -> 4, 'IX' -> 9)
            if i > 0 and current_value > rom_val[s[i-1]]:
                # Công thức: value = (current_value - 2 * previous_value)
                # Ví dụ: 'IV': int_val = 5 - 2*1 = 3 (3 là giá trị sau khi đã cộng I, giờ trừ đi 2 lần I)
                # Dễ hiểu hơn: int_val đã cộng I, giờ phải trừ I và trừ thêm I nữa
                int_val += current_value - 2 * rom_val[s[i-1]] 
            else:
                int_val += current_value
                
        return int_val

# Kiểm tra
py_solution = RomanConverter()
print(f"MMMCMLXXXVII: {py_solution.roman_to_int('MMMCMLXXXVII')}") # 3987
print(f"MCM: {py_solution.roman_to_int('MCM')}") # 1900
print(f"C: {py_solution.roman_to_int('C')}") # 100
