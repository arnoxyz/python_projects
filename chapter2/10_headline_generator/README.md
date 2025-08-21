[Back](../../)
# Clickbait Headline Generator
A a program that generates random headlines.
## How it works
It uses fixed text teamplate with a set of generated words.
```
OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
POSSESIVE_PRONOUNS = ['Her', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']
STATES = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania', 'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent', 'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado', 'Plastic Straw','Serial Killer', 'Telephone Psychic']
PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement', 'Workplace', 'Donut Shop', 'Apocalypse Bunker']
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']
```
Example of a headline generation:
```
number = random.randint(7, 15)
noun = random.choice(NOUNS)
state = random.choice(STATES)
headline = "{} Gift Ideas to Give Your {} From {}".format(number, noun, state)
```

### Example
```
python3 headlinegen.py
How many headlines do you want to generate? > 3
--------------------------------------------------------------------------------
Are Millennials Killing the Robot Industry?
You Won't Believe What This California Parent Found in Their House
9 Gift Ideas to Give Your Robot From Michigan
```
