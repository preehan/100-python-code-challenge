#Program to find out the largest digit from the number
num=int(input("Enter a number: "))
largest=0
while num>0:
    if num%10>largest:
        largest=num%10
    num//=10
print(largest)