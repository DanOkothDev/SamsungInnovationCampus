iter_num = 1

def calc_fibonacci(F, n):
    global iter_num

    print(f"\nFunction call number {iter_num}")
    print("----------------------------------------")
    print(f"{F}")

    iter_num += 1

    if n <= 1:
        return F[n]
    else:
        if F[n] < 1:
            F[n] = calc_fibonacci(F, n - 1) + calc_fibonacci(F, n - 2)
        print(f"{F[n]}")
        return F[n]

def main():
    num = int(input("\nWhich term of the Fibonacci series do you want? "))

    F = [0, 1] + [-1] * (num - 2)

    print(f"\n{F}\n")
 
    print(f"\nTerm {num} of the fibonacci series is {calc_fibonacci(F,num - 1)}")

    print(f"\n{F}\n")

if __name__ == "__main__":
    main()
       