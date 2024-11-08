employees = {'eid': 1001,'ename':'sowmya','ejob':'ceo','esalary':100000}
try:
    key = input("Enter key to access it from dictionary: ")
    value = employees[key]
    print(f"the value associated with key '{key}' is {value}")
except KeyError:
    print(f"Error: the key {key} is not found")
except Exception as e:
    print(f"unexpected error occured: {e}")
finally:
    print("Execution is succeffully competed")