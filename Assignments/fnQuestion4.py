def even(num):
    if num % 2 == 0:
        return 1
    else:
        return 0
    
def main():
    int_num = int(input("Enter a number: "))
    print(even(int_num))

main()