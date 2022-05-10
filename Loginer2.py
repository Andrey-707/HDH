# Loginer_2
from colorama import init, Fore, Back, Style

init()

print(Fore.WHITE)
print("Program start")

password = 777
running = True
while running:
	print(Fore.YELLOW)
	guess = int(input("Enter password: "))

	if guess == password:
		print(Fore.GREEN)
		print("Welcome!")
		running = False # остановить цикл while
	else:
		print(Fore.RED)
		print("Invalid password!")
else:
	print('Authorization completed.')

print(Fore.WHITE)
print("Program finish")

input()
