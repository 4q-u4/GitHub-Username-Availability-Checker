import requests
import random
import time
from colorama import Fore

while True:
    user = ""
    for character in random.choices("abcdefghijklmnopqrstuvwxyz123456789", k=3):
        user = user + character

    response = requests.get(f"https://www.github.com/{user}/")

    if response.status_code == 200:
        print(Fore.RED + f"USERNAME TAKEN: {user}" + Fore.RESET)
    elif response.status_code == 404:
        print(Fore.GREEN + f"USERNAME AVAILABLE: {user}" + Fore.RESET)
        # Append available usernames to a text file
        with open("available2usernames.txt", "a") as file:
            file.write(user + "\n")
    else:
        print("BLOCKED FROM GITHUB")
        time.sleep(120)
