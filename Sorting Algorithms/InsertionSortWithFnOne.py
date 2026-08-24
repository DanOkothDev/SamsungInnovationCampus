def insertion_sort(numbers):
    n = len(numbers)

    for i in range(1, n):
        insert_index = i
        current_value = numbers[i]
        
        for j in range(i - 1, -1, -1):
            if numbers[j] > current_value:
                numbers[j + 1] = numbers[j]
                insert_index = j
            else:
                break

        numbers[insert_index] = current_value

def main():
    mylist = [58, 36, 29, 19, 4, 14, 21, 11, 89, 9]

    print("\nBefore Sorting:\t",mylist)

    insertion_sort(mylist)

    print("After Sorting:\t", mylist)

if __name__ == "__main__":
    main()