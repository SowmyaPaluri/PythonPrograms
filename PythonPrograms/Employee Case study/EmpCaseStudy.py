import csv
current_year = 2024
list = []
with open('employee_data.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['FirstName', 'LastName', 'Year Of Birth', 'Salary', 'Bonus'])
    writer.writerow(['Alice', 'Smith', '1990', '50000', '5000'])
    writer.writerow(['Bob', 'Johnson', '1985', '60000', '4000'])
    writer.writerow(['Charlie', 'Brown', '1992', '55000', '3000'])
with open('employee_data.csv', 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)
    for row in reader:
        print(row)
        first, last = row[0], row[1]
        dob = int(row[2])
        salary = int(row[3])
        bonus = int(row[4])
        fn = f"{first} {last}"
        upsalary = salary + bonus
        age = current_year - dob
        list.append([fn, age, upsalary])
with open('updated_employee_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['FullName', 'Age', 'UpdatedSalary'])
    writer.writerows(list)
with open('updated_employee_data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
