print("simple calculator")
num1 = float(input("enter first number :"))

operator = input ("enter operator(+, -, *, /):")
num2 = float(input("enter second number:"))

if operator == "+":
    print("Result =", num1 + num2)

elif operator == "-":
    print("Result =", num1 - num2)

elif operator == "*":
    print("Result = ", num1 *num2)


elif operator =="/":
    print("Result =", num1 / num2)
else:
    print("Error! Division by zero.")


print("Invalid opeartor")




