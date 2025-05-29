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

print(get_birthdays(10))
