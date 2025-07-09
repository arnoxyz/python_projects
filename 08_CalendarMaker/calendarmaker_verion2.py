# Other implementaion of a calender maker
# New Feature: save output to a text file
import datetime

# Constants
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

def user_input(config):
    while True:
        config["month"] = input("Input a month (1,2,3...) -> ")
        if config["month"].isdigit():
            config["month"] = int(config["month"])
            break;
        else:
            print("Please insert only a digit for month")

    while True:
        config["year"] = input("Input a year(1,2,3...) -> ")
        if config["year"].isdigit():
            config["year"] = int(config["year"])
            break;
        else:
            print("Please insert only a digit for year")

    return config;



def main():
    config = {
                "month" : 6,
                "year" : 2025
    }

    config = user_input(config)
    print(config)



main()
