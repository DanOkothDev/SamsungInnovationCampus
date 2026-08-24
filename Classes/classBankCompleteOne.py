class BankAccount:
    def __init__(self, owner = "", balance = 0):
        self.__owner = owner
        self.__balance = balance
        self.__interest = 0;
        self.__new_balance = 0

    def input(self):
        self.__owner = input("Enter the name of the account owner:> ")
        self.__balance = float(input("Enter the balance in the account:> "))

    def calculate(self):
        self.__interest = 10 / 100 * self.__balance
        self.__new_balance = self.__balance + self.__interest

    def output(self):
        print(f"Account Owner: {self.__owner}")
        print(f"Account Balance Kshs.: {self.__balance:.2f}")
        print(f"Interest Kshs.: {self.__interest:.2f}")
        print(f"New Balance Kshs.: {self.__new_balance:.2f}")

def main():
    account_1 = BankAccount("Tracey Aluoch", 85900)
    account_2 = BankAccount()

    print("\nAnalysis for account 1 (the first time):")
    print("----------------------------------------------")
    account_1.calculate()
    account_1.output()

    print("\nData input for account 1: (new data)")
    print("----------------------------------------------")
    account_1.input()
    account_1.calculate()

    print("\nData input for account 2:")
    print("----------------------------------------------")
    account_2.input()
    account_2.calculate()

    print("\n\nAnalysis for account 1 (the second time):")
    print("----------------------------------------------")
    account_1.output()

    print("\nAnalysis for account 2:")
    print("----------------------------------------------")
    account_2.output()


if __name__ == "__main__":
    main()