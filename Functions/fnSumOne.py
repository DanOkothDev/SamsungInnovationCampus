def get_sum(first,second):
  total = first + second
  return total

num1 = float(input("\nEnter the first number:> "))
num2 = float(input("Enter the second number:> "))
num3 = float(input("Enter the third number:> "))
num4 = float(input("Enter the fourth number:> "))

sumOne = get_sum(num1,num2)
sumTwo = get_sum(num3,num4)

print(f"\n{num1} + {num2} = {sumOne}")
print(f"{num3} + {num4} = {sumTwo}")