import time
import os


def clear():
    # Check if Operating System is Mac and Linux or Windows
    if os.name == 'posix':
        # If OS is macOS or Linux
        _ = os.system('clear')
    else:
        # Else Operating System is Windows (os.name = nt)
        _ = os.system('cls')


def write(string: str, delay: float = 0.06):
    for i in str(string):
        print(i, end="", flush=True)
        time.sleep(delay)
    print()
