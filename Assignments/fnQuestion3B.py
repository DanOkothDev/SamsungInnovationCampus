def smallest(a, b, c):
    if a <= b and a <= c:
        small = a
    elif b <= a and b <= c:
        small = b
    else:
        small = c

    print(f"Among, {a}, {b} and {c} the smallest is {small}")
    
def main():
    num1, num2, num3 = map(int, input("Enter three numbers separated by space: ").split())

    smallest(num1, num2, num3)
    

if __name__ == "__main__":
    main()