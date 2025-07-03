# Implementaion of a calender maker
import calendar


def user_input(config):
    config["month"] = input("Input a valid month -> ");
    config["year"] = input("Input a valid year -> ");

def main():
    print("Hello World!")
    # input year and moth -> output using datetime module from python
    # fixed values for now
    config = {
                "month" : 6,
                "year" : 2025
    }

    # config = user_input(config)

    print(calendar.month(config["year"], config["month"]))

main()
