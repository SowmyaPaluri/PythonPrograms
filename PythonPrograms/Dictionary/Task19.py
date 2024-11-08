employees =[
    {'id':1001,'ename':'kiran','job':'trainer','salary':10000},
    {'id':1002,'ename':'raj','job':'developer','salary':20000},
    {'id':1003,'ename':'dev','job':'manager','salary':30000}
]

print("Menu:\n1. Display All Employee details \n2. Search employee by id \n3. Add an employee \n4. Edit an employee\n5. Delete an employee\n6. Exit\n")

while True:
    n = int(input("Enter your choice: "))
    if n == 1:
        # displaying all employees
        for e in employees:
            print(e)
    elif n == 2:
        # search employee by id
        x = int(input("Enter employee id to be searched: "))
        f = 0
        for e in employees:
            for id in e:
                if e[id] == x:
                    print("Employee found")
                    f = 1
                    break
        if f == 0:
            print("Employee not found")
    elif n == 3:
        # add an employee
        eid = int(input("Enter employee id: "))
        ename = input("Enter Employee name: ")
        ejob = input("ENter Employee job: ")
        esalary = int(input("Enter employee salary: "))
        employees.append({'id':eid,'ename':ename,'job':ejob,'salary':esalary})
    elif n == 4:
        # edit an employee
        x = int(input("Enter employee id to be edited: "))
        for e in employees:
            for id in e:
                if e[id] == x:
                    eid = int(input("Enter edited employee id: "))
                    ename = input("Enter edited Employee name: ")
                    ejob = input("ENter edited Employee job: ")
                    esalary = int(input("Enter edited employee salary: "))
                    e['id'] = eid
                    e['ename'] = ename
                    e['job'] = ejob
                    e['salary'] = esalary
                    break
            break
    elif n == 5:
        # delete an employee
        x = int(input("Enter employee id to be deleted: "))
        for e in employees:
            idx = employees.index(e)
            for id in e:
                if e[id] == x:
                    employees.pop(idx)
                    print("deleted")
    elif n == 6:
        print("Exit")
        break



