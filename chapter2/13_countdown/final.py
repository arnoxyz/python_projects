# Implementation of a countdown
import ssd, time, os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    print("Hello World!")
    for i in range(10,-1,-1):
        output = ssd.get_ssd_str(i, 2)
        clear_console()
        print(output)
        time.sleep(1)

main()
