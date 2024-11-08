# wishes based on time
def wishesBasedOnTime():
    time = input("Enter time (ex: 2 pm): ")
    hour, med = time.split()
    if med == 'am':
        print("Good morning")
    elif ((hour == '12') or (hour >= '1' and hour <= '4')) and med == 'pm':
        print("Good afternoon")
    else:
        print("Good evening")
    print()
    
wishesBasedOnTime()