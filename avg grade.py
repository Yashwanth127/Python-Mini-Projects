def cal_grade(avg):
    if avg >=90:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"
for i in range(1, 4):
    print(f"\n---Enter the detauls of students {i}---")
    name = input("Enter your student name  ")
    m1 = int(input("Enter the marks of studente 1"))
    m2 = int(input("Enter the marks of studente 2"))
    m3 = int(input("Enter the marks of studente 3"))

    average = (m1 + m2 + m3) /3
    grade = cal_grade(average)

    print("\n-- Report card ---")
    print(f"student: {name}")
    print(f"Average marks: {average:.2f}")
    print(f"grade: {grade}")
