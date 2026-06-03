import os
from colorama import Fore, init

init(autoreset=True)

os.system("clear")
userinput = input(Fore.GREEN + "select language to continue(tr/en): ").lower()
try:
    while True:
        if userinput=="en":
            from assets import eninterface as ui
            ui.baslat()
            break
        elif userinput=="tr":
            from assets import trinterface as ui
            ui.baslat()
            break
        else:
            print(Fore.RED + 'Invalid input. Please try entering “tr” or “en”.')
            break
except Exception as a:
    input(Fore.RED + "An unexpected error occurred")