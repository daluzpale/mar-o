from  datetime import date

year = int(input("Enter year: "))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("{} is ".format(year))
else:
    print("{} not a leap year".format(year))
