# datetime

import datetime as dt

# current date and time
cdt = dt.datetime.now()
print(cdt)


# current time in hours
ch = cdt.hour
print(ch)



# wishes bases on time

if ch < 12:
    print("Good Morning!")
elif ch < 16:
    print("Good Afternoon!")
else:
    print("Good Evening!")

time = input("Enter time (ex: 2 pm): ")
hour, med = time.split()
if med == 'am':
    print("Good morning")
elif ((hour == '12') or (hour >= '1' and hour <= '4')) and med == 'pm':
    print("Good afternoon")
else:
    print("Good evening")
    

