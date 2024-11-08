nums = [10,20,30,40,50]
try:
    idx = int(input("Enter index to access from list:"))
    ele = nums[idx]
    print(f"ele at index {idx} is {ele}")
except IndexError:
    print("Error: index entered is out of range")
except ValueError:
    print("Error: Invalid Input, enter valid interger")
except Exception as e:
    print(f"unexpected error occured: {e}")
finally:
    print("Execution is complete")