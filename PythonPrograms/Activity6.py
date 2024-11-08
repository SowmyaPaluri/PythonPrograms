def calculate_tax(s):
    if s < 300000:
        return 0
    elif s >= 300000 and s < 600000:
        return (s*0.05)
    elif s >= 600000 and s < 900000:
        return (s*0.1)
    elif s >= 900000 and s < 1200000:
        return (s*0.15)
    elif s >= 1200000 and s < 1500000:
        return (s*0.2)
    return s * 0.3

s = int(input("Enter your salary: "))
res = (calculate_tax(s))
print(f"The tax you have to pay is {res} from your salary {s}")
