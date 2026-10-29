# Print modified words in a list
count = int(input("Кількість слів: "))
target_length = int(input("Довжина слів для редагування: "))
char_replace = input("Символ заміни: ")

words_list = []

for _ in range(count):
    word = input().strip()
    words_list.append(word)

result_list = []

for word in words_list:
    if len(word) >= target_length:
        new_word = word[:-3] + char_replace
        result_list.append(new_word)
    else:
        result_list.append(word)

print(result_list)
