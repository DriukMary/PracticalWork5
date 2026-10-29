# Check if two words are anagrams continuously
print("Програма запущена. Для виходу натисніть Ctrl+C")

while True:
    try:
        word1 = input("Введіть перше слово: ").strip().lower()
        word2 = input("Введіть друге слово: ").strip().lower()

        is_anagram = sorted(word1) == sorted(word2)
        print(f"Результат: {is_anagram}\n")

    except KeyboardInterrupt:
        print("\nПрограму завершено!")
        break
