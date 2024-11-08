# Function as Arguments

# grade
def grade(m,p,c):
    total = m + p + c
    avg = total/3
    print(f"total: {total}")
    print(f"avg: {avg}")
    if m >= 35 and p >= 35 and c >= 35:
        print("Pass")
        if avg >= 90:
            grade = "A"
        elif avg >= 80:
            grade = "B"
        elif avg >= 70:
            grade = "C"
        elif avg >= 60:
            grade = "D"
        else:
            grade = "F"
        print(f"grade: {grade}")
    else:
        print("Fail")
        
m = int(input("Enter maths marks: "))
p = int(input("Enter physics marks: "))
c = int(input("Enter chemistry marks: "))
grade(m,p,c)