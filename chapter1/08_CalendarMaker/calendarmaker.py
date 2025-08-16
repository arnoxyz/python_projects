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

    # Weekday headers
    headers = ["SU", "MO", "TU", "WE", "TH", "FR", "SA"]
    print()
    print("|" + "|".join(["----MO----"] ) + "|", end="")
    print("" + "|".join(["----DI----"] ) + "", end="")
    print("|" + "|".join(["----MI----"] ) + "", end="")
    print("|" + "|".join(["----DO----"] ) + "", end="")
    print("|" + "|".join(["----FR----"] ) + "", end="")
    print("|" + "|".join(["----SA----"] ) + "", end="")
    print("|" + "|".join(["----SO----"] ) + "|")

    c = calendar.Calendar(firstweekday=0) # start with MO as first weekday
    weeks = c.monthdays2calendar(config["year"], config["month"])

    # Print each week
    for week in weeks:
        # First line: day number
        line1 = "|".join( f"       {day:2} " if day != 0 else "          " for (day, _) in week)
        print("|" + line1 + "|")

        # 3 blank lines per cell
        for _ in range(3):
            print("|" + "|".join(["          "] * 7) + "|")

        # Separator line
        print("+" + "+".join(["----------"] * 7) + "+") # start with MO as first weekday
    #for week in weeks:
    #    print(" ".join(f"{day:02}" if day != 0 else "  " for day in week))

main()
