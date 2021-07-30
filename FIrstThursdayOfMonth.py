# Q: Find the dates of all meeting days and print them out if they all occur on the first thursday of every month in 2021.
# To find out the dates of all the first thursday of a month in 2021
import calendar
print("The meetings are on:")
for m in range (1,13):
    k = calendar.monthcalendar(2021,m)
    weekone = k[0]
    weektwo = k[1]
    if weekone[calendar.THURSDAY] != 0:
        meetday = weekone[calendar.THURSDAY]
    elif weektwo[calendar.THURSDAY] != 0:
        meetday = weektwo[calendar.THURSDAY]
    print("%s %d" % (calendar.month_name[m], meetday))
