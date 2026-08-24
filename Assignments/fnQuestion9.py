def calculate_total():
    total = 0
    for i in range(20, 71):
        total += i

    return total

def main():
    total_sum = calculate_total()
    print(f"\nThe total is: {total_sum}\n")

if __name__ == "__main__":
    main()