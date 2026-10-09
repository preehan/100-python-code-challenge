#Program to count even numbers from 1 to n
n=int(input("Enter a number till which you want to count even numbers: "))
count=0
i=1;
while i<=n:
      if i%2==0:
        count+=1
      i+=1

print(count)
