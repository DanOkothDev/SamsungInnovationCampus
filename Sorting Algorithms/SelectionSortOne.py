def main():
    numbers = [64, 25, 12, 22, 11]

    n = len(numbers)
    
    print("\nBefore Sorting:\t",numbers)

    for i in range(n - 1):
        min_index = i
        
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
                
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
            
    print("\nAfter Sorting:\t",numbers)

if __name__ == "__main__":
    main()