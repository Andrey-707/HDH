# Progress_Bar_3
from random import uniform
from time import sleep
from rich import print
from progress.bar import IncrementalBar

print("[bold magenta]Programm start[/]")

my_list = range(10)
bar = IncrementalBar("Processing...", max=len(my_list))
for i in my_list:
    print(f"[bold cyan]\nStep[/] {i+1}")
    bar.next()
    sleep(uniform(0.1, 1))

bar.finish()

print("[bold magenta]Programm finish[/]")

input()
