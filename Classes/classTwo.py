class Employee:
    company = "Nairobi Tech"
    def __init__(self, name, age):
        self.name = name
        self.age = age

def main():
    emp1 = Employee("Patrick Otieno",45)
    emp2 = Employee("Margaret Njeri",50)
    
    print("\nEmployee 1:")
    print("------------------------");
    print(f"Name: {emp1.name}");
    print(f"Age: {emp1.age}");
    print(f"Company: {emp1.company}");

    print("\nEmployee 2:")
    print("------------------------");
    print(f"Name: {emp2.name}");
    print(f"Age: {emp2.age}");
    print(f"Company: {emp2.company}");

if __name__ == "__main__":
    main()