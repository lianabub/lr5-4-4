# Инициализация списка для хранения первых букв
new_str = []

# Ввод строки от пользователя
string = input("Введите строку для составления новой строки из первых букв слов: ")

# Разделяем строку на слова
words = string.split()

# Извлекаем первые буквы каждого слова
for word in words:
 new_str.append(word[0])  # Добавляем первую букву слова в новый список

# Преобразуем список первых букв в строку
result = ''.join(new_str)

# Вывод результата
print("Новая строка из первых букв слов:", result)