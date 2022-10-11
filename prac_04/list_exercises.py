# Question 1

numbers = []
input_numbers = 5
for number in range(input_numbers):
    enter_input = int(input("Number: "))
    numbers.append(enter_input)

print(numbers)

average_score = (sum(numbers) / len(numbers))
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {average_score:.1f} ")

# Question 2
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
             'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = str(input("Enter username: "))
if username in usernames:
    print(f"Access granted")
else:
    print(f"Access denied")
