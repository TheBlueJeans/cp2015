import calendar
year = int(input("Please enter year: \n"))
month = int(input("Please enter month: \n"))
print("The number of days in this month is:", calendar.monthrange(year, month)[1])
