# class BankAccount:
#     def __init__(self, account_number, holder_name, balance=0.0):
#         self.account_number = account_number
#         self.holder_name = holder_name
#         self.balance = balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"${amount} deposited. New balance: ${self.balance:.2f}")
#         else:
#             print("Deposit amount must be positive.")
#
#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             print(f"${amount} withdrawn. New balance: ${self.balance:.2f}")
#         else:
#             print("Invalid amount or insufficient balance.")
#
#     def apply_fee(self):
#         fee = 0.05 * self.balance
#         self.balance -= fee
#         print(f"5% bank fee applied. Fee: ${fee:.2f}. New balance: ${self.balance:.2f}")
#
#     def display(self):
#         print(f"Account Number: {self.account_number}, Holder: {self.holder_name}, Balance: ${self.balance:.2f}")
#
#
# class SavingsAccount(BankAccount):
#     def __init__(self, account_number, holder_name, balance=0.0):
#         super().__init__(account_number, holder_name, balance)
#
#     def apply_interest(self, rate=0.03):
#         interest = self.balance * rate
#         self.balance += interest
#         print(f"Interest added at 3%. New balance: ${self.balance:.2f}")
#
#
# class CheckingAccount(BankAccount):
#     def __init__(self, account_number, holder_name, balance=0.0):
#         super().__init__(account_number, holder_name, balance)
#
#     def withdraw(self, amount):
#         overdraft_limit = 500.0
#         if amount > 0 and amount <= self.balance + overdraft_limit:
#             self.balance -= amount
#             print(f"${amount} withdrawn. New balance: ${self.balance:.2f}")
#         else:
#             print("Invalid amount or overdraft limit exceeded.")



# Method Overriding in Python
class Vehicle:
    def __init__(self, model, year, condition):
        self.model = model
        self.year = year
        self.condition = condition

    def start(self):
        print("Vehicle is Starting")

class Car(Vehicle):
    def __init__(self, model, year, condition):
        super().__init__(model, year, condition)

    def start(self):
        print("Car is Starting with a Vroom")

class Bike(Vehicle):
    def __init__(self, model, year, condition):
        super().__init__(model, year, condition)

    def start(self):
      print("Bike is Starting with a Roar")

# Testing
vehicle1 = Vehicle("Toyota", 2002 , "Brand New")
vehicle1.start()

car1 = Car("Lorry", 2010, "Used")
car1.start()

bike1 = Bike("Duccati", 2023, "Brand New")
bike1.start()

# Write a Device class in Python with an init() method that takes brand and year as parameters. Then create a Phone subclass that inherits Device and adds a new attribute model. Use the super() function to call the Device initializer from the Phone class. Test it by creating a Phone object and printing out all attributes.
class Device:
    def __init__(self,brand, year):
        self.brand = brand
        self.year = year
class Phone(Device):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

    def displaying(self):
        return f"My phone is {self.model} from {self.brand} that was created in the year {self.year}"

# Phone Object
phone = Phone("Xiami", 2023, "Redmi Note 13")
print(phone.displaying())