def small(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c
    
def main():
    num1, num2, num3 = map(int, input("Enter three numbers separated by space: ").split())

    smallest = small(num1, num2, num3)
    print(f"Among, {num1}, {num2} and {num3} the smallest is {smallest}")

if __name__ == "__main__":
    main()