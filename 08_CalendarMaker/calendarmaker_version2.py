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
    h_line = ('+----------' * 7) + '+\n'
    blank_row = ('|          ' * 7) + '|\n'

    cal_str = "" #whole calendar saved as text

    #header
    cal_str += (" " * 34) + MONTHS[month - 1] + " " + str(year) + '\n'
    cal_str += "..Sunday.....Monday....Tuesday....Wednesday...Thursday.... Friday....Saturday..\n"

    #main section - week days
    current_date = datetime.date(year, month, 1)

    #go back until its sunday
    while current_date.weekday() != 6:
        current_date -= datetime.timedelta(days=1)

    while True:
        #start h_line (seperator)
        cal_str += h_line

        #day number line
        day_number_row = ""
        for i in range(7):
            day_number_label = str(current_date.day).rjust(2)
            day_number_row += "|" + day_number_label + (" " * 8)
            current_date += datetime.timedelta(days=1)
        day_number_row += "|\n"

        #add 3 empty lines
        cal_str += day_number_row
        for i in range(3):
            cal_str += blank_row

        #loop until next month starts
        if current_date.month != month:
            break

    #footer
    cal_str += h_line

    print(cal_str)
    return cal_str

def save_output(output_text, config):
    calendar_name = "calendar_{}_{}.txt".format(config["year"],config["month"])
    with open(calendar_name, "w") as file:
        file.write(output_text)
    print("Saved to " + "./"+calendar_name)



def main():
    config = {
                "month" : 6,
                "year" : 2025
    }

    config = user_input(config)
    output_text = get_calendar(config["year"], config["month"])
    save_output(output_text, config)



main()
