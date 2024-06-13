def add(x, y):
  return x + y

def subtract(x, y):
  return x - y 

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

def square(x):
  return x * x


print("Hello, world!")

# print("Welcome to the calculator!")

# while True:
#     try:
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))

#         operation = input("Enter operation (+, -, *, /): ")

#         if operation == "+":
#             add(num1,num2)
#             print(num1 + num2)

#         elif operation == "-":
#             subtract(num1,num2)
#             print(num1 - num2)

#         elif operation == "*":
#             multiply(num1,num2)
#             print(num1 * num2)

#         elif operation == "/":
#             divide(num1,num2)
#             print(num1 / num2)

#         else:
#             print("Invalid operation!")

#         restart = input("Calculate again? (y/n): ")
#         if restart == "n":
#             break

#     except ValueError:
#         print("Invalid input. Please enter numeric values only.")

# print("Bye!")