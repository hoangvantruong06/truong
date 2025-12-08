print("Hoang Van Truong\nMSV:245752021610137");
class ReverseWords:
    def reverse_words(self, s):
        # 1. Tách chuỗi thành danh sách các từ
        words = s.split()
        
        # 2. Đảo ngược thứ tự danh sách từ
        words.reverse() # words = ['py', 'hello']
        # Hoặc dùng: words = words[::-1]
        
        # 3. Nối lại các từ thành chuỗi, cách nhau bằng dấu cách
        return " ".join(words)

# Kiểm tra
py_solution = ReverseWords()
input_str = 'hello py'
print(f"Input: '{input_str}'")
print(f"Output: '{py_solution.reverse_words(input_str)}'") # 'py hello'
