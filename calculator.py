# A python code for a simple calculator

# Operators List

print("+ for Addition")
print("- for Subtraction")
print("* for Multiplication")
print("/ for Division")

# Request for users input for mathematical operator

operator = input("Input your preferred operator: ")

# Request for users number input

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Conditional Statements/Result Output
if operator == "+":
    print(num1, "+", num2, "=", (num1 + num2))

elif operator == "-":
    print(num1, "-", num2, "=", (num1 - num2))

elif operator == "*":
    print(num1, "*", num2, "=", (num1 * num2))

elif operator == "/":
    if num2 == 0:
        print("Error")
    else:
        print(num1, "/", num2, "=", (num1 / num2))

else:
    print("Enter a valid operator")
