import time
import random
import string
from tqdm import tqdm
import sys
import platform
import os
if sys.version_info.minor < 10:  
    print("[Security] - Python 3.10 or higher is recommended. The bypass will not work on 3.10+")
    print("You are using Python {}.{}".format(sys.version_info.major, sys.version_info.minor))
class NumberLetterGenerator:
    def __init__(self):
        self.values = []
    def generate(self, length):
        chars = string.ascii_letters + string.digits
        value = ''.join(random.choice(chars) for _ in range(length))
        self.values.append(value)
        return value
generator = NumberLetterGenerator()
random_str1 = generator.generate(10)
random_str2 = generator.generate(10)
random_str3 = generator.generate(10)
if platform.system() == 'Windows':
    os.system(f'cls & title {random_str1}')  
elif platform.system() == 'Linux':
    os.system('clear')  
    sys.stdout.write(f"\x1b]0; {random_str1}\x07")  
elif platform.system() == 'Darwin':
    os.system("clear && printf '\e[3J'")  
    os.system(f'''echo - n - e "\033]0;{random_str1}\007"''')  
with open('key.txt', 'r') as f:
                bruh = f.readline()
def main():
    for i in tqdm(range(1), desc='PATCHING'):
        time.sleep(random.randint(1, 2))
    os.system(f'pause & cls & title {random_str1}')
    try:
        print("""
        1.Enter with key    
        """)
        ans = input(" Selected method: ")
        if ans == "1":
            key = input( 'Enter key: ')
            if  key == bruh:
                print('\n[-] Wrong! Execute?')
                os.system(f'pause & cls  & title {random_str2}')
                next()
            else:
                print('[-] Not wrong key!')
                os._exit(1)
        else:
            print("\n[-] Wrong choice! Try again.")
            time.sleep(1)
            os.system(f'cls  & title {random_str2}')
            main()
    except KeyboardInterrupt:
        os._exit(1)
def next():
    print("\n Информация: ")
    print(" Subscripition lvl: " + "tester")
    print(f" Your key: " + bruh)
    print(f" Subscription until: " + "never")
    time.sleep(3)
    os.system(f'pause &  cls & title {random_str3}')
    print("Search process 'cs2.exe'...")
    time.sleep(3)
    print('Founded! Injecting?')
    os.system(f'pause & title {random_str3}')
    os.system('cls & title IT`S FAKE U GOT SCAMMED')
    print("Error...\n because it's a fake!")
    for _ in range(10):
         print('☺☺☺')
    time.sleep(5)
    os._exit(1)
if __name__ == "__main__":
    main()