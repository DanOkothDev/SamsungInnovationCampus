F = {0:0, 1: 1}

def fibonacci_fn(n):
    if n in F:
        return F[n]
    else:
        F[n] = fibonacci_fn(n - 1) + fibonacci_fn(n - 2)
        return F[n]

def main():
    num = int(input("\nWhich term of the Fibonacci series do you want? "))
 
    print(f"\nTerm {num} of the fibonacci series is {fibonacci_fn(num)}")

if __name__ == "__main__":
    main()
       