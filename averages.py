# the initial variables
total = 0
count = 0

# the loop to get input from user
while True:
    user_input = input("Enter a number (enter 'q' to quit): ")
    if user_input.lower() == 'q':
        break
    else:
        try:
            num = int(user_input)
            total += num
            count += 1
        except ValueError:
            print("Invalid input. Please enter a valid number or 'q' to quit.")

# calculating the average
if count != 0:
    average = total / count
else:
    average = 0

# printing the results
print(f"The sum of the numbers entered is {total}.")
print(f"The count of the numbers entered is {count}.")
print(f"The average of the numbers entered is {average}.")