class Bank:
    #class variable
    bank_name = "Default Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    # class method to change the bank name
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# Instaces before changing the bank name 
customer1 = Bank("Alice")
customer2 = Bank("Bob")

print("before changing the name:")
print(f"customer's 1 Bank: {customer1.bank_name}")
print(f"customer's 2 Bank: {customer2.bank_name}")

#changing the bank name using the class method
Bank.change_bank_name("new horizon bank")

print("\n After changing the bank name")
print(f"customer's 1 Bank: {customer1.bank_name}")
print(f"customer's 2 Bank: {customer2.bank_name}")
