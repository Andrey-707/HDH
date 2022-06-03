# Модуль string. Словарь через zip()
import string


print(string.ascii_lowercase)


list1 = [i for i in range(1, 21)]
# print(list1)
list2 = [i for i in string.ascii_lowercase]
# print(list2)

dict2 = dict(zip(list1, list2))
print(dict2)