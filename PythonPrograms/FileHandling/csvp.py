import csv
with open('ex.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name','Age','City'])
    writer.writerow(['Sowmya',22,'BVRM'])

with open('ex.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)