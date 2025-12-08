print("Hoang Van Truong\nMSV:245752021610137");
class Bank:
    # Thuộc tính cấp lớp (Class attributes)
    Account_type = "Savings"
    location = "Guntur"
    
    # Mã PIN cố định để đơn giản hóa
    PIN = 123 

    def __init__(self, name, Account_Number, balance):
        self.name = name
        self.Account_Number = Account_Number
        self.balance = balance
        # Gán thuộc tính từ Class attributes
        self.Account_type = Bank.Account_type
        self.location = Bank.location

    # Phương thức đại diện (repr) để in thông tin cơ bản
    def __repr__(self):
        return f"Tài khoản: {self.name}, Số TK: {self.Account_Number}"

    # Phương thức xử lý lỗi PIN
    def Error(self):
        print("Pin Incorrect. Please try again")
        account_pin = int(input("Please enter your pin number "))
        if account_pin == self.PIN:
            self.Account()
        else:
            self.Error() # Lặp lại

    # Phương thức xử lý các giao dịch (Menu chính)
    def Account(self):
        print("\nYour Card Number is:XXXX XXXX XXXX 1337")
        print("Would you like to deposit/withdraw/Check Balance?")
        print("------------------------------------------------")
        print("1) Balance")
        print("2) Withdraw")
        print("3) Deposit")
        print("4) Quit")
        
        while True:
            try:
                option = int(input("Please enter your choice: "))
                if option == 1:
                    self.Balance()
                elif option == 2:
                    self.Withdraw()
                elif option == 3:
                    self.Deposit()
                elif option == 4:
                    self.Exit()
                    break
                else:
                    print("Lựa chọn không hợp lệ, vui lòng chọn 1-4.")
            except ValueError:
                print("Lỗi nhập liệu. Vui lòng nhập số (1, 2, 3 hoặc 4).")


    # Phương thức kiểm tra số dư
    def Balance(self):
        print(f"\nBalance: {self.balance}")
        self.Account()

    # Phương thức rút tiền
    def Withdraw(self):
        try:
            w = int(input("\nPlease Enter Desired amount: "))
            # Kiểm tra số dư trước khi rút
            if self.balance > 0 and self.balance >= w:
                self.balance -= w
                print("Your transaction is successfull")
                print(f"Your Balance: {self.balance}")
                print("\n")
            else:
                print("Your transaction is cancelled due to")
                print("Amount is not sufficient in your account")
        except ValueError:
             print("Lỗi nhập liệu. Vui lòng nhập số tiền hợp lệ.")
             
        self.Account()
    
    # Phương thức gửi tiền
    def Deposit(self):
        try:
            d = int(input("\nPlease Enter Desired amount: "))
            self.balance += d
            print("Your transaction is successfull")
            print(f"Balance: {self.balance}")
        except ValueError:
             print("Lỗi nhập liệu. Vui lòng nhập số tiền hợp lệ.")
             
        self.Account()

    # Phương thức thoát
    def Exit(self):
        print("\nExit")
        print("Cảm ơn quý khách đã sử dụng dịch vụ!")
        

# --- Thực thi chương trình ATM ---

# 1. Tạo đối tượng ngân hàng
t1 = Bank('Mahesh', 1453210145, 5000)

# 2. Bắt đầu phiên làm việc (Yêu cầu nhập PIN)
print("Welcome to the SBI ATM Machine")
print("------------------------------")

try:
    account_pin = int(input("Please enter your pin number: "))
    
    if account_pin == t1.PIN:
        t1.Account()
    else:
        t1.Error()
except ValueError:
    print("Lỗi nhập liệu. Vui lòng nhập PIN bằng số.")
    # Có thể gọi lại t1.Error() tại đây nếu muốn thử lại
