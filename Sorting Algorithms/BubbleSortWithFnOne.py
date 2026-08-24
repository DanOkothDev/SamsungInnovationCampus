def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break

def main():
    sample_list = [64, 34, 25, 12, 22, 11, 90]

    print("\nOriginal list:\t", sample_list)
    
    bubble_sort(sample_list)

    print("Sorted list:\t", sample_list)

if __name__ == "__main__":
    main()  