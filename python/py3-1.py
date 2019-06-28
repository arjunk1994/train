from datetime import *
now=date.today()

yes=timedelta(-1)
tom=timedelta(1)

print("current date is: ")
print(now)
print("yesterday date is: ")
print(now+yes)
print("tommorows date is: ")
print(now+tom)
