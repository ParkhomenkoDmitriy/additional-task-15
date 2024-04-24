# импортируем латиницу
import string
latin_alphabet = set(string.ascii_lowercase)

user_input = input("Введите строку: ")

# Очистим строку от пробелов и приведем к нижнему регистру
cleaned_input = user_input.replace(" ", "").lower()

# Создадим множество уникальных букв из очищенной строки
input_set = set(cleaned_input)

# Проверим, на наличие всех букв латинского алфавита
if latin_alphabet.issubset(input_set):
    print("Строка является панграммой.")
else:
    print("Строка не является панграммой.")

