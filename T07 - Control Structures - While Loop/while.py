''' Use a while loop to require the user to enter a number.
Store all the input numbers in a list (except -1).
Break the iteration if the user enters the number -1.
Finally, calculate the average of all number inside the list.
'''
num_list = []

while True:
    num = int(input("Please enter a number: "))
    if num != -1:
        num_list.append(num)
    else:
        break

avg_list = sum(num_list) / len(num_list)

print(f"The average of the numbers entered (excluding -1) is: {avg_list}")
