# Phone_Book
from colorama import init, Fore, Back, Style

init()

print(Fore.WHITE)
print("Program start")

print(Fore.YELLOW)
contacts = {
# перечисляем элемены в виде словаря (пары ключ-значение)
	"89045115466" : "Andrey Barsukov",
	"89048888888" : "Ivan Ivanov",
	"89047777777" : "Petr Petrov",
}

testing = input("Введите номер абонента: ")

if testing in contacts:
	print(Fore.GREEN)
	print("Контакт найден: " + contacts[testing])
else:
	print(Fore.RED)
	print("Контакт НЕ найден!")

print(Fore.WHITE)
print("Program finish")

input()
