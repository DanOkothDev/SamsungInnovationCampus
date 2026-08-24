def main():
    numbers = [64, 25, 12, 22, 11]

    n = len(numbers)
    
    print("\nBefore Sorting:\t",numbers)

    for i in range(n - 1):
        min_index = i
        
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
                
        if min_index != i:
            temp = numbers[i]
            numbers[i] = numbers[min_index]
            numbers[min_index] = temp
            
    print("\nBefore Sorting:\t",numbers)

if __name__ == "__main__":
    main()