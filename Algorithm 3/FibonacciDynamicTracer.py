F = {0:0, 1: 1}

def fibonacci_fn(n):
    if n in F:
        print("F currently ->",F);
        return F[n]
    else:
        F[n] = fibonacci_fn(n - 1) + fibonacci_fn(n - 2)
        print("F currently ->",F);
        return F[n]

def main():
    num = int(float(input("\nWhich term of the Fibonacci series do you want? ")))
 
    print(f"\nTerm {num} of the fibonacci series is {fibonacci_fn(num)}")

if __name__ == "__main__":
    main()
       