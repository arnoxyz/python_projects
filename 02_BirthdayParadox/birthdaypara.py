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


# check if there is are two birthdays on the same date
# return true if there is one, false if there is none
def check_dublicate_birthdays(bdays): 
    for i in range(len(bdays)):
        for j in range(i + 1, len(bdays)):
            if bdays[i] == bdays[j]:
                return True
    return False

def main():
    #make my life easier with the first protoype by hardcoding: 
    bdays_number = 10 #TODO: Get Input from user: Number of Birthdays
    sim_number   = 1 #TODO: Get Input from user: Number of Simulations
    wins = 0;

    for _ in range(sim_number):
        #genBirthdays(int NumberOfBirthdays)
        birthdays = [gen_birthdays() for _ in range(bdays_number)]
        print(birthdays)

        #checkBirthday(Birthdays[]) 
        if (check_dublicate_birthdays(birthdays) == True): 
            wins+=1;

        print(wins)
        #brute foce check the birthdays O(n^2)
            #-> return 
            #   true=win (there are two birthdays on the same day)
            #   false=lose (no birthdays on the same day)

    #TODO: calcPropability
        # prop=Wins/NumberOfSims

main()
