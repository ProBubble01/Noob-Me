num1 = input ("first num here: ")
num2 = input ("second number here: ")
operation = input ("what you wanna do: ")
if operation == "+":
    result = int(num1) + int(num2)
elif operation == "-":
    result = int(num1) - int(num2)
elif operation == "*":
    result = int(num1) * int(num2)
elif operation == "/":
    result = int(num1) / int(num2)
print (result)
