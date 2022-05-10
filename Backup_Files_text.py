from colorama import init
from colorama import Fore, Back, Style
# use Colorama to make Termcolor work on Windows too
init()
print(Fore.CYAN)

# Программа для копирования (backup) файлов
print("Program start")
filename1 = input("Введите имя копируемого файла: ")
filename2 = "backup " + filename1

file1 = open(filename1, "r")
file2 = open(filename2, "w")

file2.write(file1.read())

file1.close()
file2.close()

print("Program finish")

input()