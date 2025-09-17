import calendar

# print(dir(calendar))

year = int(input("Enter an year\n"))

month = int(input("Enter a month\n"))

cal = calendar.month(year,month)

print(cal)