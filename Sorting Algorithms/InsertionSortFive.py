def main():
    numbers = [56, 134, 33, 265, 912, 242, 4, 29, 189, 16]

    print("\nBefore Sorting:\t",numbers)

    n = len(numbers)

    for i in range(1, n):
        current_value = numbers[i]  # The element to be positioned
        j = i - 1
        
        # Move elements of numbers[0..i-1] that are greater than current_value
        # to one position ahead of their current position

        while j >= 0:
            if numbers[j] > current_value:
                numbers[j + 1] = numbers[j]
            else:
                break;
            j = j - 1
            
        # Insert the current_value into its correct sorted location
        numbers[j + 1] = current_value

    print("After Sorting:\t", numbers)

if __name__ == "__main__":
    main()