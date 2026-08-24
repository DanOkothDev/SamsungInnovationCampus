def main():
    mylist = [64, 34, 25, 12, 22, 11, 90, 5]

    print("\nBefore Sorting:\t",mylist)

    n = len(mylist)

    print()

    for i in range(n - 1):
        for j in range(n - i - 1):
            if mylist[j] > mylist[j + 1]:
                mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]

            #The statement below outputs the list after every outer loop iteration
            print(mylist)

        print("----------------------------------------")

    print("\nAfter Sorting:\t", mylist)

if __name__ == "__main__":
   main()