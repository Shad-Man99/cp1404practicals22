
# Question 1
user_name = str(input("Name: "))
in_file = open("name.txt", 'w')
print(user_name, file=in_file)
in_file.close()

#  Question 2
in_file = open("name.txt")
text = in_file.read()
in_file.close()
print(text)

# Question 3
numbers_file = open("numbers.txt", 'r')
first_number = int(numbers_file.readline())
second_number = int(numbers_file.readline())
total = first_number + second_number
print(total)
numbers_file.close()

# Question 4
numbers_file = open("numbers.txt", 'r')
total = 0
for line in numbers_file:
    number = int(line)
    total += number
print(total)
numbers_file.close()
