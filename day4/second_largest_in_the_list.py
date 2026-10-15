#Program that finds the second largest number in the list
num_list=list(map(int,input("Enter numbers separated by spaces").split()))
largest = float('-inf')
second_largest = float('-inf')

for num in num_list:
    if num>largest:
        second_largest=largest
        largest=num
    elif num>second_largest and num<largest:
          second_largest=num

if second_largest==float('inf'):
         print("There is no second largest number. ")
else:
         print(f"second largest number= {second_largest}")

    
        
