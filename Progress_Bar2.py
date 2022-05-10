# Progress_Bar_2
from random import uniform
from time import sleep
from rich import print
from rich.progress import track


print("[bold magenta]Programm start[/]")

for i in track(range(11), description="Processing..."):
    print(f"[bold cyan]Step[/] {i+1}")
    sleep(uniform(0.1, 1))

print("[bold magenta]Programm finish[/]")

input()
