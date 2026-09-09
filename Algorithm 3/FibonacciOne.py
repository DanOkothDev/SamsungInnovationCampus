def fibonacci_fn(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_fn(n - 1) + fibonacci_fn(n - 2)

def main():
    num = int(input("\nWhich term of the Fibonacci series do you want? "))
 
    print(f"\nTerm {num} of the fibonacci series is {fibonacci_fn(num - 1)}")

if __name__ == "__main__":
    main()
       