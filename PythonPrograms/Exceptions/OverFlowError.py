import math
def calculate_exponential():
    try:
        res = math.exp(1000)
    except OverflowError:
        print("Error: The result is too large to represent")
    except Exception as e:
        print(f"Unexpected error occured: {e}")
    finally:
        print("Execution is complete")
        
calculate_exponential()