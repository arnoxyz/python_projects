# Calendar Maker
Generating a text output of a given calender date.

## Using the datetime Module
From the python library
(datetime Module)[https://docs.python.org/3/library/datetime.html]
This module is used to handle all the calendar related stuff:
### Gettint the current date
```
current_date = datetime.date(year, month, 1)
```
### Working with the current date
Using the current date we can go back for one day.
```
current_date -= datetime.timedelta(days=1)
```
Using this over again until we start with sunday (6).
```
while current_date.weekday() != 6:
    current_date -= datetime.timedelta(days=1)
```
## Save output text to a file
### More Verbose Way:
As I know it from C programming:
```
file = open(claendar_name, "w")
file.write(output_text)
file.close()
```
### Python Way:
Using the with syntax:
```
with ... as file:
    block to work with the file
automatically closes the file after the block (even if there's an error)
```
So using this:
```
calendar_name = "calendar_{}_{}.txt".format(config["year"],config["month"])
with open(calendar_name, "w") as file:
    file.write(output_text)
print("Saved to " + "./"+calendar_name)
```
