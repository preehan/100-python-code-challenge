#Program that checks whether a number is prime or not
n=int(input("Enter a number: "))
i=2
if n<2:
  print("not a prime number")
else:
   while i<n:
     if n%i==0:
        print("Not a Prime number")
        break
     i+=1 
   else:
        print("Prime number")
 
 