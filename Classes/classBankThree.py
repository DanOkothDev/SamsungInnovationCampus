class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Triggers name mangling

def main():
    account_1 = BankAccount("Stacey Njeri", 67500)

    print(f"\nAccount Owner: {account_1.owner}")
    print(f"Account Balance: {account_1._BankAccount__balance}")  # Using the mangled name to bypass the privacy rule

if __name__ == "__main__":
    main()