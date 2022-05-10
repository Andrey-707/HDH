# Progress_Bar_1
from random import uniform
from time import sleep
from rich import print
from rich.progress import track


print("[bold magenta]Programm start[/]")

def do_step(step):
    sleep(uniform(0.01, 0.1))

for step in track(range(100), description="Processing..."):
    do_step(step) 

print("[bold magenta]Programm finish[/]")

input()
