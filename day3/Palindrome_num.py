#Program that tells whether a number is palindrome or not
num=int(input("Enter a number: "))
number=num
num_reverse=0

while num>0:
    digit=num%10
    num_reverse=num_reverse*10+digit
    num=num//10

if num_reverse==number:
    print("Palindrome number") 
else:
    print("Not a Palindrome")
