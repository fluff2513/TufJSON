import json
import questionary
from rich import print
import subprocess

subprocess.run("clear")
print("[cyan1]T[/cyan1][cyan2]u[/cyan2][medium_spring_green]f[/medium_spring_green][spring_green1]J[/spring_green1][spring_green2]S[/spring_green2][green1]O[/green1][green3]N[/green3] - The [bold]TUFFIEST[/bold] JSON file formater!")
json_ = questionary.text("Insert the JSON text :").ask()
name = questionary.text("What is the file name? :").ask()
dictionnary = json.loads(json_)
formate = json.dumps(dictionnary, indent=4)

with open(f"{name}.json", "w") as f:
    f.write(formate)
    
print(f"""[bright_green]Your JSON file succesfully create! :)[/bright_green]
Made by @Fluff2513 on GitHub.""")
