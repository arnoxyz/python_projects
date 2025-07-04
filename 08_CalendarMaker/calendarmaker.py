# Implementaion of a calender maker
import calendar

def user_input(config):
    month = 0
    year = 0

    while True:
        month = input("Input a month (1,2,3...) -> ")
        if month.isdigit():
            break;
        else:
            print("Please insert only a digit for month")

    while True:
        year = input("Input a year(1,2,3...) -> ")
        if year.isdigit():
            break;
        else:
            print("Please insert only a digit for year")

    config["month"] = int(month)
    config["year"] = int(year)
    return config;


def main():
    config = {
                "month" : 6,
                "year" : 2025
    }

    config = user_input(config)
    print(calendar.month(config["year"], config["month"]))

main()
