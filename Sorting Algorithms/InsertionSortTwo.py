def main():
    mylist = [64, 34, 25, 12, 22, 11, 90, 5]

    print("\nBefore Sorting:\t",mylist)

    n = len(mylist)
    print("\n")

    for i in range(1, n):
        insert_index = i
        current_value = mylist[i]
        
        for j in range(i-1, -1, -1):
            if mylist[j] > current_value:
                mylist[j+1] = mylist[j]
                mylist[j] = "_" #This line added for illustration only 
                insert_index = j
                print(mylist)
            else:
                break

        mylist[insert_index] = current_value
        print(mylist)
        print("--------------------------------------")

    print("\n\nAfter Sorting:\t", mylist)

if __name__ == "__main__":
    main()