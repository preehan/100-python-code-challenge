#Program that print fibonanci series
n=int(input("Enter a number"))
if n<=0:
    print("Enter a positive number.")
else:
     a=0
     b=1
     i=0
     while i<n:
       print(a)
       c=a+b
       a=b
       b=c
       i+=1