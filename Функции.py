# Функции
from colorama import init, Fore, Back, Style


init()

print(Fore.MAGENTA)
print("Program start")

print(Fore.YELLOW)
# 1.Примеры стандартных функций:
str() # string - строка
float() # float - дробное число
list() # list - список
function(1, 2, 3, 4) # function - функция

def print_spam(): # def = defined
	print("spam")
	print("spam")
	print("spam")

print_spam() # вызываем функцию
print_spam() # вызываем функцию повторно

# 2.Параметр функции
# Значения, вызванные в определении функции (например, number) называются ПАРАМЕТРОМ ФУНКЦИИ
def multiply(number): # parametr
	print(number*2)
# Числа, заключенные в multiply называются АРГУМЕНТАМИ ФУНКЦИЙ
multiply(2) # argument

def multiply(number): # parametr
	print(number*5)

multiply(4) # argument

# 3.Метод return (вернуть)
def max(x, y):
	if x > y:
		return x
	else:
		return y
print(max(5, 10)) # OUT: 10

# 4.Использование переменных в каместве аргументов функции.
def max(x, y):
	if x > y:
		return x
	else:
		return y
x = float(input("Число x = "))
y = float(input("Число y = "))
print(max(x, y)) # На печать выводится большее число в формате float

# 5.Исключения.
# Функция не сработает, посольку в коде не существует переменной 'num'.
# Переменная 'num' обьявлена в коде локально (отдельно от функции)
def test():
	num = 10
test()
print(num) # NameError: name 'num' is not defined

# 6.Функция отработает до return и выведет только цифры 1 и 2
def print_numbers():
	print(1)
	print(2)
	return # функция ни чего не возвращает
	print(3)
	print(4)
print_numbers()

# 7.assert (утверждение)
def exc(text):
	print(str(text) + "!")
exc("Hello World") # функция добавит восклицательный знак к тексту

# Необходимо ввести текст.
def exc(text):
	assert text != "", "Вы не ввели текст."
	print(str(text) + "!")
exc("") # Не передаем тект - получаем ошибку AssertionError: Вы не ввели текст.

# Необходимо ввести число > 0.
def test(number):
	assert number > 0, "Число меньше нуля."
	print(str(number))
test(-10) # Числа < 0 - получаем ошибку AssertionError: Число меньше нуля.

print(Fore.MAGENTA)
print("Program finish")

input()
