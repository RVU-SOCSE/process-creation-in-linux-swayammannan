#CALCULATOR
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

match op:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        print(a / b)
    case _:
        print("Invalid operator")

#TEMPERATURE CONVERSION
temp = float(input("Enter temperature value: "))
unit = input("Convert to (C/F): ")
match unit.upper():
    case "C":
        print((temp - 32) * 5/9, "°C")
    case "F":
        print((temp * 9/5) + 32, "°F")
    case _:
        print("Invalid choice")

#largest among 3 numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
print("Largest:", largest)

#smallest 3 numbers 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

print("Smallest:", smallest)
