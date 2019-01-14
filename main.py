import os, platform
import time
import colorama
import sys

# Stores console's window size at launch
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 35

# Console functions >
# Configures console's window size according to platform
def set_console_size():
    if platform.system() == 'Windows':
        os.system('title ASCII Combat')
        os.system(f'mode con: cols={SCREEN_WIDTH} lines={SCREEN_HEIGHT}')
    elif platform.system() == 'Linux' or platform.system() == 'Darwin':
        os.system('echo -n -e "\033]0;ASCII Combat\007"')
        os.system(f'echo "\033[8;{SCREEN_HEIGHT};{SCREEN_WIDTH}t"')

# ASCII functions >
# Clears screen according to platform
def clear():
        print(colorama.Style.BRIGHT + colorama.Back.BLACK + colorama.Fore.WHITE, end='')
        if platform.system() == 'Windows':
            os.system('cls')
        elif platform.system() == 'Linux' or platform.system() == 'Darwin':
            os.system('clear')

# Returns an ANSI Sequence to change cursor position
def pos(x, y):
    return f'\x1b[{y};{x}H'


def main():
    set_console_size()
    print(pos(5, 15))
    print('Hello World!')
    input()
    # # game = combat.Combat(me, enemies)
    # # game.cmdloop()

if __name__ == '__main__':
    main()  

