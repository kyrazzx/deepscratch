import os
import time
import shutil
import requests
import json
from colorama import Fore, Style, init
from itertools import cycle

init(autoreset=True)

BASE_URL = "https://api.scratch.mit.edu/users"

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_ascii_art_with_animation():
    art = r"""
________                        _________                    __         .__     
\______ \   ____   ____ ______ /   _____/ ________________ _/  |_  ____ |  |__  
 |    |  \_/ __ \_/ __ \\____ \\_____  \_/ ___\_  __ \__  \\   __\/ ___\|  |  \ 
 |    `   \  ___/\  ___/|  |_> >        \  \___|  | \// __ \|  | \  \___|   Y  \
/_______  /\___  >\___  >   __/_______  /\___  >__|  (____  /__|  \___  >___|  /
        \/     \/     \/|__|          \/     \/           \/          \/     \/  
    """
    console_width = shutil.get_terminal_size().columns
    colors = cycle([Fore.RED, Fore.LIGHTRED_EX])

    for _ in range(10):
        clear_console()
        color = next(colors)
        for line in art.splitlines():
            print(color + line.center(console_width))
        time.sleep(0.2)

    print(Fore.RED + "Made by Kyra".center(console_width))

def progress_bar(current, total, bar_length=40):
    percent = int(current / total * 100)
    bar = ('█' * int(bar_length * percent / 100)).ljust(bar_length)
    print(Fore.LIGHTRED_EX + f"[{bar}] {percent}% Complete", end="\r")

def interactive_menu():
    while True:
        clear_console()
        print(Fore.RED + "Main Menu".center(shutil.get_terminal_size().columns, "-"))
        print(Fore.LIGHTRED_EX + "[1] Start User Info Analysis")
        print(Fore.LIGHTRED_EX + "[2] Exit")
        choice = input(Fore.RED + "Choose an option: ")
        if choice == "1":
            return
        elif choice == "2":
            clear_console()
            print(Fore.RED + "Thanks for using my tool!".center(shutil.get_terminal_size().columns))
            time.sleep(2)
            exit()
        else:
            print(Fore.LIGHTRED_EX + "Invalid option!".center(shutil.get_terminal_size().columns))
            time.sleep(2)

def write_analysis_to_file(username, analysis):
    filename = f"analysis_{username}.txt"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(analysis)

def format_json(data):
    return json.dumps(data, indent=4)

def get_user_info(username):
    url = f"{BASE_URL}/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_user_favorites(username):
    url = f"{BASE_URL}/{username}/favorites"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_user_followers(username):
    url = f"{BASE_URL}/{username}/followers"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_user_following(username):
    url = f"{BASE_URL}/{username}/following"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_user_projects(username):
    url = f"{BASE_URL}/{username}/projects"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_user_messages(username, filter_type=None):
    url = f"{BASE_URL}/{username}/messages"
    if filter_type:
        url += f"?filter={filter_type}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_user_studios(username):
    url = f"{BASE_URL}/{username}/studios/curate"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def generate_analysis(username):
    analysis = f"Analysis of {username}'s Scratch Profile\n"
    analysis += "=" * 80 + "\n\n"
    analysis += f"Username: {username}\n"
    analysis += "=" * 80 + "\n"

    steps = [
        ("User Info", get_user_info),
        ("Favorites", get_user_favorites),
        ("Followers", get_user_followers),
        ("Following", get_user_following),
        ("Projects", get_user_projects),
        ("Messages", get_user_messages),
        ("Studios", get_user_studios)
    ]
    
    total_steps = len(steps)
    for step_number, (label, func) in enumerate(steps, start=1):
        analysis += f"\n{'-' * 80}\n"
        analysis += f"{label}:\n"
        analysis += "=" * 80 + "\n"
        data = func(username)
        if data:
            analysis += format_json(data) + "\n"
        else:
            analysis += f"No data available for {label}.\n"
        
        progress_bar(step_number, total_steps)
    
    write_analysis_to_file(username, analysis)
    print(Fore.GREEN + f"Analysis saved to analysis_{username}.txt")

def main():
    username = input(Fore.RED + "Enter the Scratch username: ")
    clear_console()
    generate_analysis(username)

if __name__ == "__main__":
    clear_console()
    display_ascii_art_with_animation()
    time.sleep(1)
    interactive_menu()
    main()
