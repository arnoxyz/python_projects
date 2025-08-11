# Implementaion of clickbait headline genrator
import random

def get_input():
    while True:
        user_input = input("How many headlines do you want to generate? > ")
        if user_input.isdigit():
            return int(user_input)


def main():
    print("Hello World")
    print(get_input())

main()
