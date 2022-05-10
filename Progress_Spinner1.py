# Progress_Spinner_1
from time import sleep
from rich import print
from rich.console import Console

print("[bold magenta]Program start[/]")

console = Console()
tasks = [f"Task {n}" for n in range(1, 11)]

with console.status("[bold green]Working on tasks...[/]") as status:
	while tasks:
		task = tasks.pop(0)
		sleep(1)
		console.log(f"{task} complete.")

print("[bold magenta]Program finish[/]")

input()
