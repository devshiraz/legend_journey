print("Welcome to the Legendary Calculator.")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Select operation +, -, *, /")
op = input("Operation: ")

if op == "+":
    print("Result: ", a + b)
elif op == "-":
    print("Result: ", a - b)
elif op == "*":
    print("Result: ", a * b)
elif op == "/":
    print("Result: ", a / b)
else:
    print("Unknown operation. The spell fails.")
