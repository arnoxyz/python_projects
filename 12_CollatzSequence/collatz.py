# Generation of the collatz sequence

def get_user_input():
    while True:
        number = input("Insert start integer > ")
        if number.isdigit():
            return int(number)

def main():
    number = get_user_input()
    print(number)

main()
