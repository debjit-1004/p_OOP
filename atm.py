class Atm:
    #static variable
    counter=1

    def __init__(self):              #constructor is init ; special method that is automatically executed when an object is created
        self.__pin=" "
        self.__balance=0
        self.sno=Atm.counter
        Atm.counter +=1
        print(self.sno)

        self.__menu()

    def __menu(self):
        user_input=int(input(''' How will you like to proceed:
                                1. To create pin
                                2. To deposit
                                3. Withdraw
                                4. Check balance 
                                5. exit () '''))

        if user_input==1:
            self.create_pin()
        elif user_input==2:
            self.deposit()
        elif user_input==3:
            self.withdraw()
        elif user_input == 4:
           self.check_balance()
        elif user_input == 5:
            print('exit!')
        else:
            print('error')


    def create_pin(self):
        temp=input('Enter your pin')
        self.__pin=temp
        print('pin set successfully')
        self.__menu()

    def deposit(self):
        temp=input("Enter your pin")
        if temp==self.__pin:
             self.__balance +=int(input('Enter the amount you want ot deposit '))
             print('Money successfully deposited ')
        else:
            print('wrong pin entered ')
        self.__menu()

    def withdraw(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            amount = int(input("enter the amount you want to withdraw"))
            if amount < self.__balance:
                self.__balance -= amount
                print(amount , 'successfully withdrawn')
            else:
                print('Not sufficient balance ')

        else:
            print("Invalid pin ")

        self.__menu()

    def check_balance(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            print("The balance in your account is:", self.__balance)

        self.__menu()








sbi= Atm()
hdfc=Atm()

