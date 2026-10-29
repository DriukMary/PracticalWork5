# Prints all even numbers from a list until it encounters 0 or a stop number 'n'.


numbers_input = input("Enter the numbers separated by spaces: ")

text_list = numbers_input.split()

numbers_list = []

for x in text_list:
    number = int(x)
    numbers_list.append(number)

n = int(input(" Input number n: "))

for i in numbers_list:
    if i == n or i == 0:
        break

    if i % 2 == 0:
        print(i)
