def smallest_num(a, b, c):
    if a <= b and a <= c:
        small =  a
    elif b <= a and b <= c:
        small = b
    elif c <= a and c <= b:
        small = c
    
    return small

num1, num2, num3 = map(float, input("Enter three numbers: ").split())

smallest = smallest_num(num1, num2, num3)

print(f"The smallest number is: {smallest}")