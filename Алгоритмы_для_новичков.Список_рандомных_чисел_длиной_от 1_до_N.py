# Алгоритмы для новичков. Рандомный список в пределах от 1 до N.
import random


N = int(input("Укажие длину списка: "))
nums = list()

for i in range(N):
	nums.append(random.randint(1, N))

print(nums)

input()
