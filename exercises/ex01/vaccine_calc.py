"""A vaccination calculator."""

__author__ = "730400485"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...

today: datetime = datetime.today()
pop = int(input("Population: "))
dosesadministered = int(input("Doses administered: "))
dosesperday = int(input("Doses per day: "))
targetpercent = int(input("Target percent vaccinated: "))
today: datetime = datetime.today()
days = int((pop - dosesadministered)/dosesperday)
days_delta: timedelta = timedelta(int(days))
future: datetime = today + days_delta
print("We will reach "+ str(targetpercent) + "% vaccination in " + str(days) + " days, which falls on " + str(future.strftime("%B %d, %Y")) + ".")