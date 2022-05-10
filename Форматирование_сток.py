# Форматирование строк
from colorama import init, Fore, Back, Style


init()

print(Fore.MAGENTA)
print("Program start")

print(Fore.YELLOW)
# 1.Конкатенация строк
name = "Андрей"
age = 35
print("Привет, " + str(name) + "!") # OUT: Привет, Андрей!
print("Тебе уже " + str(age) + " лет.") # OUT: Тебе уже 35 лет.
'''либо'''
print("Привет, " + str(name) + "!\nТебе уже " + str(age) + " лет.")

# 2.Форматирование строк. %, placeholder 
name = "Андрей"
age = 35
print("Привет, %s!\nТебе уже %i лет." % (name, age))
# после значка % идет placeholder. placeholder - это такая строка, коорая удерживает
# данное место и в будующем будет заенена на реальные данные. В нашем случае два
# placeholer это %s (s - placeholder стоки) и %d(или %i) (d - placeholder десятичного
# числа), также еть %f (f - placeholder дробного числа)

# 3.Форматирование строк. Метод .format()
name = "Андрей"
age = 35
print("Привет, {0}!\nТебе уже {1} лет.".format(name, age))
print("Привет, {}!\nТебе уже {} лет.".format(name, age)) # индексы 0, 1 указывать необязательно (так нумеруются по умолчанию)

# Повторение подстроки в строке
print("{0}{1}{0}".format("abra","cad")) # OUT: abracadabra

# Арифметические операции
a = 10
b = 3
c = a + b
print("{0} + {1} = {2}".format(a, b, c)) # OUT: 10 + 3 = 13
print("{} + {} = {}".format(a, b, c)) # индексы 0, 1, 2 указывать необязательно (так нумеруются по умолчанию)

# Форматирование строк. С указанием переменной.
person_name = "Андрей"
person_age = 35
print("Привет, {name}!\nТебе уже {age} лет.".format(name=person_name, age=person_age))

# 4.Форматирование строк. С использованием словаря.
person = {
	"name" : "Adrey",
	"age" : 35
}
print("Имя: {name}\nВозраст: {age}".format(name=person["name"], age=person["age"]))

# Ещё один способ с использованием словаря.
human = {
	"name" : "Adrey",
	"age" : 35
}
print("Имя: {person[name]}\nВозраст: {person[age]}".format(person=human))

# 5.Заполнение строки сиволами *** или ___ по длине строки.
# Если не ставить символ заполнения, то строка заполнится пробелами.
"""
   Andrey   
***Andrey***
___Andrey___
___Andeson__
Ansaahoiarss
Anasfafasf__
"""
input_str = "Andrey"
print("Hello {0}!".format(input_str)) # OUT: Hello Andrey!

# Правое заполнение <
input_str = "Andrey"
print("Hello {0:*<12}!".format(input_str)) # OUT: Hello Andrey******!

# Левое заполнение >
input_str = "Andrey"
print("Hello {0:*>12}!".format(input_str)) # OUT: Hello ******Andrey!

# Центрированное заполнение ^
input_str = "Andrey"
print("Hello {0:_^12}!".format(input_str)) # OUT: Hello ___Andrey___!

# 6.Равномерное центрированное заполнение ^
# Отцентрируем имя "Jessy" вручную, нам поребуется 11 ячеек
input_str = "Jessy"
print("Hello {0:_^11}!".format(input_str))

# Допустим, что мы хотим отцентрировать имя  на 10 ячеек
# ставим в переменную length = 10
input_str = "Jessy"
length = 10
print("Длина строки: " + str(len(input_str))) # OUT: Длина строки: 5
print("Результат деления по модулю: " + str(len(input_str) % 2)) # OUT: Результат деления по модулю: 1
if len(input_str) % 2:
	length += 1 # length = 11
# програма автоматически ценрирует имя "Jessy" и добавляет +1 ячейку
print(("Hello {0:_^"+str(length)+"}!").format(input_str)) # OUT: Hello ___Jessy___!

print(Fore.MAGENTA)
print("Program finish")

input()
