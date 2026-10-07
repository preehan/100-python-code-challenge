#largest  of three numbers
a=float(input("Enter a  number"))
b=float(input("Enter a  number"))
c=float(input("Enter a  number"))

if a>b and a>c:
     print(f"{a} is the largest.")
elif b>a and b>c:
     print(f"{b} is the largest.")
else:
     print(f"{c} is the largest")
