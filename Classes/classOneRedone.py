class Employee:
    def __init__(self):
        self.name =  ""
        self.age = 0;

def main():
    emp1 = Employee()

    print(f"Name: {emp1.name}");
    print(f"Age: {emp1.age}");

if __name__ == "__main__":
    main()