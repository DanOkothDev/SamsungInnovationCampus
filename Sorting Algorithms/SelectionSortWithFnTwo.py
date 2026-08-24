def selection_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]

def main():
    numbers = [64, 96, 25, 12, 32, 9, 22, 11]  

    print("\nBefore Sorting:\t",numbers)

    selection_sort(numbers)
    
    print("\nAfter Sorting:\t",numbers)

if __name__ == "__main__":
    main()