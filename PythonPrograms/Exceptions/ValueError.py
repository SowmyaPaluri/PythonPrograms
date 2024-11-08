def get_integer_input():
    try:
        ipt = input("Enter an integer: ")
        num = int(ipt)
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
        num = None
    else:
        print("input is a valid integer")
    finally:
        print("Execution is completed for input")
    return num

n = get_integer_input()
if n is not None:
    print(f"number is {n}")
else:
    print("No valid integer was entered")