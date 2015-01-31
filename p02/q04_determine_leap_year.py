import calendar
year = int(input("Please enter year: \n"))
if calendar.isleap(year)==True:
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))
