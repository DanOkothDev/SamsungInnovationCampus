# This program prints all the elements in the fibonacci series up to the specified element 

def fibonacci_fn(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_fn(n - 1) + fibonacci_fn(n - 2)

def main():
    num = int(input("\nHow many terms of the Fibonacci series do you want? "))

    print()
 
    for i in range(num):
        print(fibonacci_fn(i), end = " ")

    print()

if __name__ == "__main__":
    main()
       