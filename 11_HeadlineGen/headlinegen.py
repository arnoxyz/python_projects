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

def gen_headline(number_of_headlines):
    for i in range(number_of_headlines):
        headline_number = random.randint(1,7)
        headline = get_headline(headline_number)
        print(headline)

def get_headline(number):
    headline = ""

    if number == 1:
        noun = random.choice(NOUNS)
        headline = "Are Millennials Killing the {} Industry?".format(noun)
    elif number == 2:
        noun = random.choice(NOUNS)
        pluralNoun = random.choice(NOUNS) + 's'
        when = random.choice(WHEN)
        headline = "Without This {}, {} Could Kill You {}".format(noun, pluralNoun, when)
    elif number == 3:
        pronoun = random.choice(OBJECT_PRONOUNS)
        state = random.choice(STATES)
        noun1 = random.choice(NOUNS)
        noun2 = random.choice(NOUNS)
        headline = "Big Companies Hate {}! See How This {} {} Invented a Cheaper {}".format(pronoun, state, noun1, noun2)
    elif number == 4:
        state = random.choice(STATES)
        noun = random.choice(NOUNS)
        pronoun = random.choice(POSSESIVE_PRONOUNS)
        place = random.choice(PLACES)
        headline = "You Won\'t Believe What This {} {} Found in {} {}".format(state, noun, pronoun, place)
    elif number == 5:
        pluralNoun1 = random.choice(NOUNS) + 's'
        pluralNoun2 = random.choice(NOUNS) + 's'
        headline = "What {} Don\'t Want You To Know About {}".format(pluralNoun1, pluralNoun2)
    elif number == 6:
        number = random.randint(7, 15)
        noun = random.choice(NOUNS)
        state = random.choice(STATES)
        headline = "{} Gift Ideas to Give Your {} From {}".format(number, noun, state)
    elif number == 7:
        number1 = random.randint(3, 19)
        pluralNoun = random.choice(NOUNS) + 's'
        number2 = random.randint(1, number1)
        headline = "{} Reasons Why {} Are More Interesting Than You Think (Number {} Will Surprise You!)".format(number1, pluralNoun, number2)

    return headline


def main():
    print("Hello World")
    #number_of_headlines = get_input()
    number_of_headlines = 1
    gen_headline(number_of_headlines)

main()
