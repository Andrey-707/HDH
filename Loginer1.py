# Loginer_1
from colorama import init, Fore, Back, Style

init()

print(Fore.WHITE)
print("Program start")

print(Fore.YELLOW)

quess = input("Enter password: ")
password = "Andrey"
while quess != password:	
	print(Fore.RED)
	print("Invalid password!")
	print(Fore.YELLOW)
	quess = input("Enter password: ")
else:
	print(Fore.GREEN)
	print("Welcome!")

print(Fore.WHITE)
print("Program finish")

input()
