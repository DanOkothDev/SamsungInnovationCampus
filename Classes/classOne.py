class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def main():
    emp1 = Employee("Patrick Otieno",45)
    
    print(f"Name: {emp1.name}");
    print(f"Age: {emp1.age}");

if __name__ == "__main__":
    main()