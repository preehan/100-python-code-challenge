#Program to check the voting eligibility
age=int(input("Enter your age in years:"))
if age<0:
   print("Invalid input!!!")
elif age>=18:
  print("You are eligible to vote!")
else:
   print("You are not eligible to vote!")

