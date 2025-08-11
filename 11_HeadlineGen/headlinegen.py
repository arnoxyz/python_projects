# Implementaion of clickbait headline genrator
import random

#constants
OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
POSSESIVE_PRONOUNS = ['Her', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']
STATES = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania', 'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent', 'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado', 'Plastic Straw','Serial Killer', 'Telephone Psychic']
PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement', 'Workplace', 'Donut Shop', 'Apocalypse Bunker']
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']

def get_input():
    while True:
        user_input = input("How many headlines do you want to generate? > ")
        if user_input.isdigit():
            return int(user_input)

def gen_headline():
    headline = random.randint(1,8)
    print(headline)


def main():
    print("Hello World")
    #number_of_headlines = get_input()
    number_of_headlines = 1

    for i in range(number_of_headlines):
        gen_headline()

main()
