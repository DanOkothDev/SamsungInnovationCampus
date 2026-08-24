class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance  # Intended as private/protected

def main():
    account_1 = BankAccount("Stacey Njeri", 67500)

    print(f"\nAccount Owner: {account_1.owner}")
    print(f"Account Balance: {account_1._balance}")  # Works, but discouraged by convention

if __name__ == "__main__":
    main()