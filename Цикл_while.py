# Цикл while
from colorama import init, Fore, Back, Style


init()

print(Fore.MAGENTA)
print("Program start")

print(Fore.YELLOW)
# 1.Бесконечный цикл
# Создаем условие, при котором отработает print()
test = True
if test :
	print("something")

# При условии (test = True) цикл while будет бесконено выводить print()
while test :
	print("somewhere")
	test = False # Останавливаем цикличность условием False

# 2.Условия для отстановки цикла while
# Вывести на экран в строку последовательно 1, 2, 3, 4, 5
i = 1
while i <= 5:
	print(i, end=", ") # OUT: 1, 2, 3, 4, 5
	i = i + 1

# 3.Остановить цикл while при помощи break
i = 1
while 1 == 1: # бесконечно
	print("Привет! " + str(i))
	i += 1
# когда i достигнет значения > 10, а именно 11 условие перестает выполняться
	if i > 10:
		break

# 4.Пропустить. continue
# Вывести на экран ТОЛЬКО четные числа до 10 включительно
number = 0
while number <= 10:
	number += 1
	if number % 2 != 0: # если число делится на 2 без остатка, то оно является четным
		continue
	print("Четное число " + str(number)) 

print(Fore.MAGENTA)
print("Program finish")

input()
