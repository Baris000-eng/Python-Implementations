print("Enter the month for which you want to create the calendar and \nenter also the year of this month: ")
yil = int(input("Year: "))
ay = int(input("Month: "))
 

import calendar

print(calendar.month(yil, ay))