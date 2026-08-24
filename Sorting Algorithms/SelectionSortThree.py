def main():
    numbers = [64, 25, 12, 22, 11]

    n = len(numbers)
    
    print("\nBefore Sorting:\t",numbers)

    print()

    for i in range(n - 1):
        for j in range(i + 1, n):
            if numbers[j] < numbers[i]:
                numbers[j], numbers[i] = numbers[i], numbers[j]

            print(numbers)
        print("------------------------------")
            
    print("\nAfter Sorting:\t",numbers)

if __name__ == "__main__":
    main()