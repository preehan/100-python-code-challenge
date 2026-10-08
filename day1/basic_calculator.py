#Simple calculator
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
op=input("Enter the operator ('+','-','x','/'):")

def add(a,b):
  a=num1
  b=num2
  return a+b

def minus(a,b):
   a=num1
   b=num2
   return a-b

def mul(a,b):
   a=num1
   b=num2
   return a*b

def div(a,b):
   a=num1
   b=num2
   return a/b

if op[0]=='+':
  print(f"The sum of two numbers={add(num1,num2)}")

elif op=='-':
   print(f"The difference is={minus(num1,num2)}")

elif op=='x':
   print(f"Multiplication is:{mul(num1,num2)}")

elif op=='/':
   print(f"The result of division is:{div(num1,num2)}")

else:
   print("Enter the correct operator")




