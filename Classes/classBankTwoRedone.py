class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance

    def display(self):
        print(f"\nAccount Owner: {self.__owner}")
        print(f"Account Balance: {self.__balance}")

def main():
    account_1 = BankAccount("Stacey Njeri", 67500)

    account_1.display()

if __name__ == "__main__":
    main()