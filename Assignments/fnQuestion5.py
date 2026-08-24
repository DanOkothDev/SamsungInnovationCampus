def get_big(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
def main():
    num1, num2, num3 = map(float, input("Enter three numbers: ").split())

    big = get_big(num1, num2, num3)
    print(f"The biggest number among: {num1}, {num2} and {num3} is {big}")

main()