# grade of student
m,p,c = map(int,input().split())
total = m + p + c
avg = total/3
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
    print(grade)
else:
    print("Fail")
