import calendar

cal = calendar.TextCalendar(calendar.SUNDAY)

while True:
    year = int(input("Enter year: "))

    month = int(input("Enter month: "))

    print(cal.formatmonth(year, month))

    r = input("Do you want to run again? (y/n) ")
    if r != "y":
        break