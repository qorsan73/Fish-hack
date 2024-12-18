import os
import colorama
from colorama import Fore,Style
import time
import sys
from art import tprint

def convert_to_python_logo(text):
    tprint(text, font="block")
def slow_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
mostafa = ("QORSAN")

convert_to_python_logo(mostafa)
slow_print(Fore.RED + "Wait a few seconds please......", delay=0.05)
time.sleep(5)
os.system("clear")
os.system("python qfk.py")
