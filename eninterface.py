import requests
from colorama import Fore, Style, init
from bs4 import BeautifulSoup
import os
import pyperclip

init(autoreset=True)

try:
    while True:
        os.system("clear")
        # print(Fore.GREEN + Style.BRIGHT + "=========================================")
        # print(Fore.GREEN + Style.BRIGHT + "          WikiAI ASSISTANT v1.0          ")
        # print(Fore.GREEN + Style.BRIGHT + "        Developed by devtoprak (2026)       ")
        # print(Fore.GREEN + Style.BRIGHT + "=========================================\n")
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        userinput = input(Fore.CYAN + Style.BRIGHT + "Search on Wikipedia: ").capitalize()
        
        r = requests.get('https://en.wikipedia.org/wiki/' + userinput, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        paragraphs = soup.select('.mw-parser-output > p')
        
        if paragraphs:
            print("\n" + Fore.BLUE + "="*40 + "\n")
            
            counter = 0
            for p in paragraphs:
                if p.text.strip():
                    print(Fore.YELLOW + Style.BRIGHT + p.text)
                    print()
                    counter += 1
                    
                if counter == 2:
                    break
            
            print(Fore.BLUE + "="*40 + "\n")
        else:
            print(Fore.RED + "No summary found for the requested topic!\n")
            continue
        qoc = input(Fore.CYAN + Style.BRIGHT + "Press 'q' to quit, 'c' to continue, Press the 'k'key to copy: ").lower()
        if qoc == "q":
            print(Fore.GREEN + "Exiting WikiAI. Goodbye!")
            break
        elif qoc == "c":
            continue
        elif qoc == "k":
            pyperclip.copy(soup.find('p').text)
            print(Fore.BLUE + "The text was successfully copied!")
            continue
        else:
            input(Fore.RED + Style.BRIGHT + "Invalid input! Closing the application.")
            break

except Exception as a:
    print(Fore.RED + Style.BRIGHT + "An unexpected error occurred!")
    input(Fore.GREEN + Style.BRIGHT + "Press Enter to exit...")