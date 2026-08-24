def average(m1, m2, m3):
    avg = (m1 + m2 + m3) / 3
    return avg

def get_grade(avg_marks):
    if avg_marks >= 80 and avg_marks <= 100:
        grade = "A"
    elif avg_marks >= 70:
        grade = "B"
    elif avg_marks >= 60:
        grade = "C"
    elif avg_marks >= 50:
        grade = "D"
    elif avg_marks >= 0:
        grade = "E"

    return grade

def main():
    score1, score2, score3 = map(float, input("Enter three marks separated by comas: ").split(","))

    average_score = average(score1, score2, score3)
    grade_score = get_grade(average_score)

    print(f"The average score is: {average_score}, calculating to a grade {grade_score}")

if __name__ == "__main__":
    main()