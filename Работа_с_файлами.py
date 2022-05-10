# Работа с файлами.
from colorama import init, Fore, Back, Style

init()

print(Fore.MAGENTA)
print("Program start")

print(Fore.YELLOW)
# 1.Режимы открытия фала.
#1) r (read) - режим чтения файла.
#2) w (write)- режим перезаписи файла.
#3) a (append) - режим добавления информации в файл.
#4) b (binary) - бинарный режим.
#5) len (length) - режим для подчета количества символов в файле.

# 2.Чтение файлов.
# Чтобы прочитать файл в python используется функция open. Режим чтения "r"
file = open("Test1.txt", "r")
print(file.read())
file.close()

input()

# Используем функцию input для указания имени файла. Режим чтения "r"
file = open(input("Введите имя файла: "), "r")
print(file.read())
file.close()

input()

# 3.Подсчет символов в файле.
# Чтобы подсчитать число символов в текстовом файле используем функцию len
file = open("Test1.txt", "r")
print("В данном текстовом файле " + str(len(file.read())) + " символов.")
file.close()

input()

# 4.Создание файла (перезапись файла).
# При ипользовании функции "w" если файл НЕ сущестует, он будет создан.
# Если файл существует, он будет пересоздан (предыдущий файл будет перезаписан на новый).
file = open("Test2.txt", "w")

# 5.Создание файла (перезапись файла). Добавление информации в файл.
# Пересоздаем файл
file = open("Test2.txt", "w")
# Пишем текстовое содержимое файла
file.write(input("Введите содержание файла: "))
file.close()

input()

# Считываем новую информацию из файла
file = open("Test2.txt", "r")
print(file.read())
file.close()

input()

# Счиаем число символов в файле
file = open("Test2.txt", "r")
print("В данном текстовом файле " + str(len(file.read())) + " символов.")
file.close()

input()

# 6.Побайтовое чтение файла
# Одна буква/символ файла равняется 2 байт
file = open("Test2.txt", "r")
print("Читаю 10 Байт")
print(file.read(7)) # читаем 10 байт файла = Привет!
file.close()

input()

# При наличии ограниченного количества оперативной памяти ожно читать файл по
# 1 Килобайт (1024 Байт) сегментами, например по 10 раз
file = open("Test2.txt", "r")
print("Читаю 10 раз по 1 Килобайт")
print(file.read(1024) *10)
file.close()

input()

# 7.Создание файла (дозапись в файл).
# С помощью функции append можно дописать содержимое в файл
file = open("Test2.txt", "a")
print("Режим дозаписи.")
file.write(" Информация снова дополнена.")
file.close()

input()

# Считываем новую информацию из файла
file = open("Test2.txt", "r")
print(file.read())
file.close()

input()

# 8.Копирование текстовых файлов
filename1 = input("Имя копируемого файла: ")
filename2 = input("Имя нового файла (копии): ")
file1 = open(filename1, "r")
file2 = open(filename2, "w")
file2.write(file1.read())
file1.close()
file2.close()

input()

# 9.Построковое чтение файла. Вариант №1
# В данном режиме текст будет выглядеть в виде списка. Каждая строка будет отдельным элементом спсиска.
# Отображаются символы переноса строки.
file = open("Test1.txt", "r")
strings = file.readlines()
print(strings)
file.close()

input()

# Построковое чтение файла. Вариант №2
file = open("Test1.txt", "r")
strings = file.readlines()
for string in strings:
	print(string)
file.close()

input()

# 10.Метод with..as
# Этот метод в конце программы закрывает файл автоматически.
with open("Test1.txt", "r") as f:
	print(f.read())

print(Fore.MAGENTA)
print("Program finish")

input()
