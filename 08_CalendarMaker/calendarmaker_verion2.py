# Other implementaion of a calender maker
# New Feature: save output to a text file
import datetime

# Constants
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

def user_input(config):
    while True:
        config["month"] = input("Input a month (1,2,3...) -> ")
        if config["month"].isdigit() and int(config["month"]) >= 1 and int(config["month"]) <= 12:
            config["month"] = int(config["month"])
            break;
        else:
            print("Please insert only a digit for month (1,2,3,...,11,12)")

    while True:
        config["year"] = input("Input a year(1,2,3...) -> ")
        if config["year"].isdigit():
            config["year"] = int(config["year"])
            break;
        else:
            print("Please insert only a digit for year")
    return config

def get_calendar(year, month):
    cal_str = "" #whole calendar saved as text

    #header
    cal_str += (" " * 34) + MONTHS[month - 1] + " " + str(year) + '\n'
    cal_str += "...Sunday.....Monday....Tuesday...Wednesday...Thursday.... Friday....Saturday..\n"
    print(cal_str)



def main():
    config = {
                "month" : 6,
                "year" : 2025
    }

    #config = user_input(config)
    get_calendar(config["year"], config["month"])


main()
