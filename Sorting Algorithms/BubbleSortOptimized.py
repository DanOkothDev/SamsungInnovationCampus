def main():
    mylist = [7, 3, 9, 12, 11]

    print("\nBefore Sorting:\t",mylist)

    n = len(mylist)

    print()

    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if mylist[j] > mylist[j + 1]:
                mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
                swapped = True
            print(mylist) # Included for illustration purpose only.

        if not swapped:
            break
            
        print(f"----------------------------------------")

    print("\nAfter Sorting:\t", mylist)

if __name__ == "__main__":
   main()