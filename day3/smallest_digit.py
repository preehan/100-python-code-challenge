#Program that finds the smallest digit in a number
num=int(input("Enter a number:  "))
smallest=num%10
while num>0:
    if num%10<smallest:
        smallest=num%10
    num//=10
print(smallest)