def cal_grade(marks ):
    if marks >= 90:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 50:
        return "C"
    else :
        return "Fail"

name = input ("enter Your name: ")
marks = int(input("Enter Your marks "))

grade = cal_grade(marks )
print ("\n --- Report card ---")
print (f"student : {name }")
print (f"marks {marks }")
print (f"Grade: {grade}")
