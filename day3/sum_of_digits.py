#Program that calculates the sum of digit
number=int(input("Enter a number: "))
total=0
while number>0:
    total+=number%10  
    number=number//10 
print(total)
    