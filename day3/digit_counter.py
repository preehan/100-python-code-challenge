#Program that calculates number of digits
num=int(input("Enter a number: "))
no_digits=0
i=0
if num==0:
    no_digits=1

while num>0:
    num=num//10
    no_digits+=1
    i+=1
print(no_digits)