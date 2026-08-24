class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Triggers name mangling

def main():
    account_1 = BankAccount("Stacey Njeri", 67500)

    print(f"\nAccount Owner: {account_1.owner}")
    print(f"Account Balance: {account_1.__balance}")  # This will raise an AttributeError

if __name__ == "__main__":
    main()