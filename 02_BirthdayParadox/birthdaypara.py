# Simulate Birthdayparadox
import random
from datetime import date, timedelta

#gen and return birthdays
def gen_birthdays():
    base_year = 2001  # Non-leap year
    start_date = date(base_year, 1, 1)
    end_date = date(base_year, 12, 31)

    random_days = random.randint(0, (end_date - start_date).days)
    random_date = start_date + timedelta(days=random_days)

    # Format: day.month (e.g., 5.3 for 5th March)
    return f"{random_date.day}.{random_date.month}"

def main():
    #make my life easier with the first protoype by hardcoding: 
    bdays_number = 10 #TODO: Get Input from user: Number of Birthdays
    sim_number   = 1 #TODO: Get Input from user: Number of Simulations

    #TODO: add loop number of sim here
    print("bla")
    #genBirthdays(int NumberOfBirthdays)
    birthdays = [gen_birthdays() for _ in range(bdays_number)]
    print(birthdays)

        #TODO: checkBirthday(Birthdays[]) 
            #-> return 
            #   true=win (there are two birthdays on the same day)
            #   false=lose (no birthdays on the same day)
    #TODO: calcPropability
        # prop=Wins/NumberOfSims

main()
