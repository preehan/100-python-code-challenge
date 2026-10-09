#Program to calculate the sum of even numbers from 0 to n
n=int(input("Enter a number: "))
sum=0
i=0

while i<=n:
    if  i%2==0:
        sum=sum+i
    i+=1

print(sum)