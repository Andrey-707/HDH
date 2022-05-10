# Работа со сроками и числами.
from rich import print

print("[bold magenta]Programm start[/]")
# Работа со строками. Методы строк.
# 1.Сепаратор и символ окончания строки.
hour = 1
minute = 5
second = 12
print(hour, minute, second, sep=":", end="\n") # OUT: 1:5:12

# Добавим к выводу текста формат
print("%02d:%02d:%02d" % (hour, minute, second)) # OUT: 01:05:12

input()

# 2.Преобразование списка к строке. Метод .join()
fruits = ["lemons", "apples", "kiwi", "pineapples", "strawberry"]
# Перед методом указываем символ-разделитель (например, запятая ","), внутрь метода помещаем список.
print(", ".join(fruits)) # OUT: lemons, apples, kiwi, pineapples, strawberry

# Выберем в качестве символа-разделителя " - ".
fruits = ["lemons", "apples", "kiwi", "pineapples", "strawberry"]
print(" - ".join(fruits)) # OUT: lemons - apples - kiwi - pineapples - strawberry

input()

# 3.Преобразование строки к списку. Метод .split()
members = "James, Jonny, Jessie, Jack, John"
# (",") указывает на то, что слова в исходной строке соеденены символом запятой
print(members.split(",")) # OUT: ['James', 'Jonny', 'Jessie', 'Jack', 'John']

input()

# 4.Строка начинается с определенной буквы. Метод .startswith()
name = "Andrey" # в этом случае имя начинается с английской "А"
# Метод .startswith() регистрозависим (с "А" или с "а").
if name.startswith("A"):
	print("Ваше имя начинается с буквы 'A'.")
else:
	print("Ваше имя начинается НЕ с буквы 'A'.")

input()

# 5.Строка заканчивается на определенную букву. Метод .endswith()
name = "Andrey" # в этом случае имя заканчивается на английскую "y"
# Метод .endswith() регистрозависим (на "Y" или на "y").
if name.endswith("y"):
	print("Ваше имя заканчивается на букву 'у'.")
else:
	print("Ваше имя НЕ заканчивается на букву 'у'.")

input()

# 6.Преобразование текста к строчным (маленьким) буквам. Метод .lower()
name = "Andrey" # в этом случае имя начинается с английской "А"
# Метод .lower() снимает с текста зависимость от регистра.
if name.lower().startswith("a"):
	print("Ваше имя начинается с буквы 'A'.")
else:
	print("Ваше имя начинается НЕ с буквы 'A'.")

# В данном случае НЕ важно рус или англ раскладка.
name = "Аndrey" # в этом случае имя начинается с русской "А"
# Снова снимаем с текста зависимость от регистра при помощи метода .lower()
if name.lower().startswith("а") or name.lower().startswith("a"):
	print("Ваше имя начинается с буквы 'A'.")
else:
	print("Ваше имя начинается НЕ с буквы 'A'.")

# Метод .lower() переводит ВЕСЬ текст в нижний регистр.
some_text = "AnDrEy"
print(some_text.lower()) # OUT: "andrey"

input()

# 7.Преобразование текста к прописным (большим) буквам. Метод .upper()
name = "Andrey"
# Метод .upper() снимает с текста зависимость от регистра.
# В данном случае НЕ важно рус или англ раскладка.
if name.upper().startswith("А") or name.upper().startswith("A"):
	print("Ваше имя начинается с буквы 'A'.")
else:
	print("Ваше имя начинается НЕ с буквы 'A'.")

input()

# 8.Замена символа (или символов) в строке. Метод .replace()
# Заменим имя Петр на имя Андрей.
print("Hello, Peter!".replace("Peter", "Andrey"))

input()

# 9.Функции для работы с числами.

# Метод min()
# Вывод на печать минимальное число из списка.
print(min([1, 3, 6, 9, 15, 122])) # OUT: 1

# Метод max()
# Вывод на печать максимальное число из списка.
print(max([1, 3, 6, 9, 15, 122])) # OUT: 122

# Абсолютное число (модуль числа). Метод abs()
# Вывод на печать число без каких-либо знаков.
print(abs(-122)) # OUT: 122

# Метод sum()
# Вывод на печать сумму чисел списка .
print(sum([1, 3, 6, 9, 15, 122])) # OUT: 156

print() # пустая строка

print("[bold magenta]Programm finish[/]")

input()
