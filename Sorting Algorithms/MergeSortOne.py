def merge_sort(arr):
    # Base case: A list with 0 or 1 elements is already sorted
    if len(arr) <= 1:
        return arr

    # 1. Divide: Find the midpoint and split the array
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_half = arr[:6]
    print(left_half, end = " ")
    print(right_half)

    # 2. Conquer: Recursively sort both halves
    merge_sort(left_half)
    merge_sort(right_half)

    # 3. Merge: Combine the sorted halves back into the original array
    i = j = k = 0

    # Compare elements from left and right halves
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Collect any remaining elements from left_half
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    # Collect any remaining elements from right_half
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

def main():
    data = [38, 27, 43, 3, 9, 82, 10]

    print(f"Original array: {data}")

    merge_sort(data)

    print(f"Sorted array:   {data}")

if __name__ == "__main__":
    main()