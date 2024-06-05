
print("Calculator")
import math
print("+ : Sum")
print("- : Subtract")
print("* : Multiply")
print("/ : Division")
print("sqrt")
print("sin")
print("cos")
print("tan")
print("cot")
print("factorial")
operation = input()
if operation == "+" or operation =="-" or operation == "*" or operation == "/":
     Number_1 = float(input("Please enter the first number"))
     Number_2 = float(input("Please enter the second number"))
     if operation == "+": print(Number_1 + Number_2) 
     elif operation == "-": print(Number_1 - Number_2) 
     elif operation == "*": print(Number_1 * Number_2) 
     elif operation == "/": print(Number_1 / Number_2) 
else: 
     a = float(input("Please enter the first number:")) 
     if operation == "sqrt":
          print(math.sqrt(a)) 
     elif operation == "sin": 
          b = math.radians(a)
          print(math.sin(b)) 
     elif operation == "cos":
          b = math.radians(a)
          print(math.cos(b)) 
     elif operation == "tan":
          b = math.radians(a)
          print(math.tan(b)) 
     elif operation == "cot":
          b = math.radians(a)
          print(math.sin(b))
     elif operation == "factorial":
          print(math.factorial(a))