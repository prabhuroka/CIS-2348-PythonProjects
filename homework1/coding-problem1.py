#Prabhu Roka
#1986444
from datetime import datetime
print("Birthday Calculator")
print("Current day")
current_month = int(input("Month: "))
current_day = int(input("Day: "))
current_year = int(input("Year: "))
print("")
print("Birthday")
birth_month = int(input("Month: "))
birth_day = int(input("Day: "))
birth_year = int(input("Year: "))

current_date = datetime(current_year, current_month, current_day)
birth_date = datetime(birth_year, birth_month, birth_day)
age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))
print(f"You are {age} years old.")
if current_month == birth_month and current_day == birth_day:
    print("Happy Birthday!")

