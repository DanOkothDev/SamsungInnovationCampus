def average_func(a, b, c):
    avg = (a + b + c) / 3
    return avg

def grade_score(avg):
    if avg >= 70:
        grade = "A"
    elif avg >= 60:
        grade = "B"
    elif avg >= 50:
        grade ="C"
    elif avg >= 40:
        grade = "D"
    else:
        grade = "F"
    return grade
    
mark1, mark2, mark3 = map(float, input("Enter the marks: ").split())

average = average_func(mark1, mark2,mark3)
grade = grade_score(average)

print()
print(f"The average is: {average:.2f} and the grade is {grade}\n")