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
    a= float(input("Enter first number: "))
    b= float(input("Enter second number: "))
    