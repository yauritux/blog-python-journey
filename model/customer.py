from datetime import date
from middleware.processing_time import processing_time
from middleware.logger import Logger

class Customer:

    def __init__(self, fname: str, lname: str, gender: bool):
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.__dob = None

    def set_dob(self, dob):
        self.__dob = dob

    def get_dob(self):
        return self.__dob

    def register(self):
        print(f"Registered {self.lname}, {self.fname} into the system.")

    def __str__(self):
        return f"\nCustomer Fullname: {self.lname}, {self.fname}\n\
Gender: {'Male' if self.gender is True else 'Female'}\nDate of Birth: {self.__dob}\n"


class CustomerAccount(Customer):

    # disclaimer (this doesn't represent a real bank name)
    bank_name = "Bank-RUPT"

    def __init__(self, fname: str, lname: str, gender: bool, \
                 acc_no: str, acc_type: str):
        super().__init__(fname, lname, gender)
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.__balance = 0

    # this method will override it's parent `register` method
    def register(self):
        print(f"Opened a new bank account for {self.fname} {self.lname}.")

    def current_balance(self):
        return self.__balance

    @processing_time
    def withdraw(self, amt: float):
        if self.__balance < amt:
            raise Exception("Balance is not sufficient!")

        self.__balance -= amt
        print(f"{amt} is withdrawn from your account.")
        print(f"Your balance now is {self.__balance}")

    @processing_time
    def deposit(self, amt: float):
        if amt <= 0:
            raise Exception("Deposit amount should be greater than 0.00!")

        self.__balance += amt
        print(f"{amt} has been added into your account.")
        print(f"Your balance now is {self.__balance}")
  
    @Logger
    def compare_customer_balance(cust1, cust2):
        if cust1.current_balance() > cust2.current_balance():
            return cust1
     
        return cust2
    
    @Logger
    def calculate_credit_score(cust) -> float:
        if cust.current_balance() > 0 and cust.current_balance() < 1000:
            return 0.01
        if cust.current_balance() > 1000 and cust.current_balance() <= 10000:
            return 0.05
        if cust.current_balance() > 10000 and cust.current_balance() <= 50000:
            return 0.10
        if cust.current_balance() > 50000 and cust.current_balance() <= 100000:
            return 0.25
        if cust.current_balance() > 100000:
            return 0.50

        return 0.00            
    
    def __str__(self):
        return f"{super().__str__()}Account Number: {self.acc_no}\nType of Account: {self.acc_type}\nCurrent Balance: {self.__balance}"
    
    def __lt__(self, other) -> bool:
        return True if self.__balance < other.current_balance() else False
    
    def __eq__(self, other) -> bool:
        return True if self.acc_no == other.acc_no \
            and self.acc_type == other.acc_type else False
    
    def __call__(self, *args, **kwargs):
        print(self)
  

if __name__ == "__main__":
    # use class attribute / field
    # notice that you can directly access the class attribute 
    # without creating any instance
    print(f"Welcome to {CustomerAccount.bank_name}!\n")

    # creating two CustomerAccount instances / objects by calling the class's constructor
    # (i.e. the  __init__ method)
    first_customer: Customer = CustomerAccount("Yauri", "Attamimi", True, "911007212", "DEPOSIT_ACCOUNT")
    second_customer = CustomerAccount("Bruce", "Lee", True, "911007213", "DEPOSIT_ACCOUNT")
    third_customer = CustomerAccount("Jackie", "Chan", True, "911007212", "DEPOSIT_ACCOUNT")

    second_customer.set_dob(date(1973, 7, 20))

    # try to withdraw an amount of $70,000 from first customer's account
    try:
        first_customer.withdraw(70000)
    except Exception as e:
        print(f"{e}")

    # check first customer's balance
    print(first_customer.current_balance())

    # deposit $90,000 to customer's first account
    first_customer.deposit(90000)

    # print out first and second customer's current balance
    print(f"First customer current balance is: {first_customer.current_balance()}")
    print(f"Second customer current balance is: {second_customer.current_balance()}")

    # compare two customer's balance of account and returns the greater one.
    # (calling CustomerAccount's class method directly without creating an instance)
    print(CustomerAccount.compare_customer_balance(first_customer, second_customer))

    print(first_customer < second_customer)

    print(first_customer == third_customer)

    first_customer()
    second_customer()

    from typing import List

    customers: List[Customer] = list()

    customers.append(Customer("Go Kou", "Son", True))
    customers.append(CustomerAccount("Yauri", "Attamimi", True, "911212007", "DEPOSIT"))

    for customer in customers:
        customer.register()
