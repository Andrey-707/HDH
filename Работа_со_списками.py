# Работа со списками.
from colorama import init, Fore, Back, Style

init()

print(Fore.MAGENTA)
print("Program start")

print(Fore.YELLOW)
# 1.Списки. Приведем пример списка, состоящего из целых чисел.
test = [1, 2, 3, 4, 5]
print(test)

# Вывести на экран цифру 1 из списка. Индекс первого элемента равен 0.
print(test[0])

# Список в списке.
part = [1, 2, 3, [4, 5, 6]]

# Вывести на экран цифру 5. Индекс четвертого элемента (второго списка) равен 3
# и во втором списке индекс второго элемента равен 1.
print(part[3][1])

# Вывести на экран букву "d".
name = "Andrey"
# Индекс буквы "d" равен 2.
print(name[2])

# 2.Применение математических оператров к спискам.
test = [1, 2, 3]
print(test * 2) # OUT: [1, 2, 3, 1, 2, 3]
print(test + [4, 5, 6]) # OUT: [1, 2, 3, 4, 5, 6]

# 3.Элементами списков так же могут быть и строки.
List = ["Alex Mercer", "Tony Stark", "Lenny Flawes"]

# Положительное условие: Чтобы выяснить есть ли в имеющемся списке имя Tony Stark
if "Tony Stark" in List:
	print("Tonny Stark is in list!")

# Выполним то же самое со списком чисел.
List2 = [1, 2, 3, 5, 6]

# Положительное условие: Есть ли цифра 4 в списке? Овет "False"
if 4 in List2:
	print("True")
else:
	print("False")

# Отрицательное условие: чтобы выяснить нет ли цифры 4 в списке. Ответ "True"
if 4 not in List2:
	print("True")
else:
	print("False")

# 4.Добавление элементов в список.
# У нас есть пустой список. Необходимо заполнить или дополнить его новыми элементами.
test = []

test.append(1)
test.append(2)
test.append(3)
test.append([4, 5, 6])

print(test) # OUT: [1, 2, 3, [4, 5, 6]]

# 5.Колечество элементов в списке (длина списка).
test = [3, 2, 4, 8, 5, 7, 6]
print(test) # OUT: [3, 2, 4, 8, 5, 7, 6]
print("В списке 'test' " + str(len(test)) + " элементов.") # OUT: В списке 'test' 7 элементов.

# Добавляем один элемент 1. Элемент добавляется в конец списка.
test.append(1)
print(test) # OUT: [3, 2, 4, 8, 5, 7, 6, 1]
print("В списке 'test' " + str(len(test)) + " элементов.") # OUT: В списке 'test' 8 элементов.

# Удаление элементов.
# Чтобы удалить число 6 из списка применим метод списка .remove(6)
test.remove(6)
print(test) # OUT: [3, 2, 4, 8, 5, 7, 1]
print("В списке 'test' " + str(len(test)) + " элементов.") # OUT: В списке 'test' 7 элементов.

# 6.Добавление, замена элементов списка.
test = [1, 3, 4, 5, 6, 7]

# Добавляем число 2 в конец списка
test.append(2)
print(test) # OUT: [1, 3, 4, 5, 6, 7, 2]

# Удалим число 2 из списке
test.remove(2)
print(test) # OUT: [1, 3, 4, 5, 6, 7]

# Добавим число 2 на свое порядковое место (вставим в список по индексу).
test.insert(1, 2)
print(test) # OUT: [1, 2, 3, 4, 5, 6, 7]

# 7.Поиск минимума и максимума в списке.
test = [1, 2, 3, -123, 123]

# Поиск минимума.
print(min(test)) # OUT: -123 

# Поиск максимума.
print(max(test)) # OUT: 123

# Подсчет элементов в списке (повтор элементов).
print(test.count(3)) # OUT: 1

# 8.Переворачивание списка.
test = [5, 4, 3, 2, 1]

# Чтобы перевернуть список воспользуемся методом списка .reverse()
test.reverse()
print(test)

# 9.Список числовой последовательности.
# Сгенерируем список  последовательности от 1 до 100
numbers = range(100)
print(numbers) # OUT: range(0, 100)

# Чтобы привести числовую последовательность к виду списка
numbers = list(range(101)) # т.к. последний элемент 101 не входит, то (range(101)
print(numbers) # OUT: [0, 1, 2, ..., 100]

# Чтобы получить числовую последовательность в виде списка
numbers = list(range(50, 101)) # OUT: [50, 51, 52, ..., 100]
print(numbers)

# Чтобы получить список четных чисел от 0 до 100
numbers = list(range(0, 101, 2))
print(numbers) # OUT: [0, 2, 4, 6..., 100]

# Чтобы получить список НЕчетных чисел от 1 до 99
numbers = list(range(1, 101, 2))
print(numbers) # OUT: [1, 3, 5, 7..., 99]

print(Fore.MAGENTA)
print("Program finish")

input()
