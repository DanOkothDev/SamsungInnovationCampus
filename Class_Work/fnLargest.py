def largest(a, b):
    if a > b:
        large = a
    else:
        large = b
    return large
num1, num2 = map(float, input("Enter two numbers: ").split())

largest_num = largest(num1, num2)
print(f"The largest numbers is: {largest_num}")    