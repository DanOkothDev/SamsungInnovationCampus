class Employee:
    def __init__(self, name = "", age = 0):
        self.name =  name
        self.age = age

def main():
    emp1 = Employee("Patrick Otieno",45)
    emp2 = Employee()

    print("\nEmployee 1:")
    print("------------------------");
    print(f"Name: {emp1.name}");
    print(f"Age: {emp1.age}");

    print("\nEmployee 2:")
    print("------------------------");
    print(f"Name: {emp2.name}");
    print(f"Age: {emp2.age}");

if __name__ == "__main__":
    main()