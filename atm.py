class Atm:
    # Static variable (Class variable shared among all instances)
    counter = 1

    def __init__(self):
        # Encapsulation (Private instance variables)
        self.__pin = " "
        self.__balance = 0
        self.__transaction_history = []
        self.sno = Atm.counter
        Atm.counter += 1
        print(self.sno)
        self.__menu()

    def __menu(self):
        # Abstraction (Hiding implementation details from the user)
        user_input = int(input(''' How will you like to proceed:
                                1. Create PIN
                                2. Deposit
                                3. Withdraw
                                4. Check Balance
                                5. Change PIN
                                6. View Transaction History
                                7. Exit
                                '''))

        if user_input == 1:
            self.create_pin()
        elif user_input == 2:
            self.deposit()
        elif user_input == 3:
            self.withdraw()
        elif user_input == 4:
            self.check_balance()
        elif user_input == 5:
            self.change_pin()
        elif user_input == 6:
            self.view_transaction_history()
        elif user_input == 7:
            print('Exit!')
        else:
            print('Error')

    def create_pin(self):
        # Encapsulation (Private method)
        temp = input('Enter your new PIN: ')
        self.__pin = temp
        print('PIN set successfully')
        self.__menu()

    def deposit(self):
        # Encapsulation (Private method)
        temp = input("Enter your PIN: ")
        if temp == self.__pin:
            amount = int(input('Enter the amount you want to deposit: '))
            self.__balance += amount
            self.__transaction_history.append(f"Deposited: {amount}")
            print('Money successfully deposited')
        else:
            print('Wrong PIN entered')
        self.__menu()

    def withdraw(self):
        # Encapsulation (Private method)
        temp = input("Enter your PIN: ")
        if temp == self.__pin:
            amount = int(input("Enter the amount you want to withdraw: "))
            if amount <= self.__balance:
                self.__balance -= amount
                self.__transaction_history.append(f"Withdrew: {amount}")
                print(amount, 'successfully withdrawn')
            else:
                print('Not sufficient balance')
        else:
            print("Invalid PIN")
        self.__menu()

    def check_balance(self):
        # Encapsulation (Private method)
        temp = input("Enter your PIN: ")
        if temp == self.__pin:
            print("The balance in your account is:", self.__balance)
        else:
            print("Invalid PIN")
        self.__menu()

    def change_pin(self):
        # Encapsulation (Private method)
        temp = input("Enter your current PIN: ")
        if temp == self.__pin:
            new_pin = input("Enter your new PIN: ")
            self.__pin = new_pin
            print("PIN changed successfully")
        else:
            print("Invalid current PIN")
        self.__menu()

    def view_transaction_history(self):
        # Encapsulation (Private method)
        temp = input("Enter your PIN: ")
        if temp == self.__pin:
            print("Transaction History:")
            for transaction in self.__transaction_history:
                print(transaction)
        else:
            print("Invalid PIN")
        self.__menu()

# Creating instances of Atm (Instantiation of objects)
sbi = Atm()
hdfc = Atm()

