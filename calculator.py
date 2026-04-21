def add(a, b):
    return a + b
def subtract(a, b):   
     return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b
if __name__ == "__main__":
    print("simple calculator running in docker")
try:

    a= float(input("Enter first number: "))
    b= float(input("Enter second number: "))
    
    print("addition:", add(a, b))
    print("subtraction:", subtract(a, b))
    print("multiplication:", multiply(a, b))
    print("division:", divide(a, b))
     
except ValueError: 
    print("error: please enter valid numbers")

except Exception as e:
    print("unexpected error:", e)    