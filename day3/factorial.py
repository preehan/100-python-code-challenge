#Factorial of a number
n=int(input("Enter the number to calculate its factorial: "))
fact=1
if n==0:
    print("Factorial of 0 is 1")
elif n!=0 and n>0:
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
else:
    print("Factorial of a negative number does not exist.")
