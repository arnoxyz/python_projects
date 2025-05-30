# Simulate Birthdaypara version2
import datetime, random


def get_birthdays(number_of_birthdays):
    birthdays = []
    for i in range(number_of_birthdays):
        # just use the same year (year is not important)
        year = datetime.date(2001, 1, 1)
        random_amount_of_days = datetime.timedelta(random.randint(0, 364)) 

        new_bday = year + random_amount_of_days
        birthdays.append(new_bday)
    return birthdays;

def get_match(birthdays):
    # creates a set of the birthday list (so duplicates get removed)
    # then checks if both lists are equal length
    if len(birthdays) == len(set(birthdays)):
        return False

    # if the two lists are not of equal length => there is a duplicate (same birthday)
    return True

def get_bdays_input():
    print("Hom many brithdays should be generated? (Max 100))")
    while True:
        bdays_input = input("> ")
        if bdays_input.isdecimal() and (0 < int(bdays_input) <= 100):
            break;
        print("Wrong Input!! -> needs to be a integer value between (0,100]")
    return int(bdays_input)


bdays_count = get_bdays_input()
bdays_dates = get_birthdays(bdays_count)

# print out the generated birthdays
for birthday in bdays_dates:
    date_text = "[{}.{}] ".format(birthday.day, birthday.month)
    print(date_text)

