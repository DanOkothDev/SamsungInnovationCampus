class Employee:
    def __init__(self, jina, miaka):
        self.__name = jina
        self.age = miaka

def main():
    
    emp1= Employee("Patrick Otieno",45)

    print(f"Name: {emp1._Employee__name}");
    print(f"Age: {emp1.age}");

if __name__ == "__main__":
    main()