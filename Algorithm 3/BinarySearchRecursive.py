def binary_search(arr, target, low = 0, high = low):
    # Initializing high for the first call.
    if high == -1:
        high = len(arr) - 1

    # Target was not present in the list
    if low > high:
    	return -1
    else:
        # Calculate the middle index
        mid = (low + high) // 2
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            return binary_search(arr, target, mid + 1, high)
            
        # If target is smaller, ignore right half
        else:
            return binary_search(arr, target, low, mid - 1)

def main():
    my_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target_val = 23

    result = binary_search(my_list, target_val)

    if result == -1:
        print(f"\nElement {target_val} not found!\a")
    else:
        print(f"\nElement {target_val} found at index: {result}")

if __name__ == "__main__":
   main()