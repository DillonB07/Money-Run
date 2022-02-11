import time
import os


def clear():
    # Check if Operating System is Mac and Linux or Windows
    _ = os.system('clear') if os.name == 'posix' else os.system('cls')


def write(string: str, delay: float = 0.06):
    for i in str(string):
        print(i, end="", flush=True)
        time.sleep(delay)
    print()
