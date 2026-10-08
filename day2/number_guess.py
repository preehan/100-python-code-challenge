#Program that checks the guess of a number
secret_num=8
n=int(input("Enter a number: "))
if n==secret_num:
    print("You guessed the right number.")
elif n<secret_num:
    print("Guess is quite low")
else:
    print("Guess is too high")
