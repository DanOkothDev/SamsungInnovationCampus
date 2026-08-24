from fnQuestion2A import average


def grade(avg):
    if avg >= 80 and avg <= 100:
        print("Your grade is : A\n")
    elif avg >= 70:
        print("Your grade is : B\n")
    elif avg >= 60:
        print("Your grade is : C\n")
    elif avg >= 50:
        print("Your grade is : D\n")
    elif avg >= 0:
        print("Your grade is : E\n")

def main():
    mark1, mark2, mark3 = map(float, input("Enter three marks, separated by coma: ").split(","))

    avg_marks = average(mark1, mark2, mark3)

    grade(avg_marks)
    
if __name__ == "__main__":
    main()