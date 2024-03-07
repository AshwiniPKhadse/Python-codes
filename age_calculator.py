'''import calendar
from datetime import datetime

def calculate_age(birth_day, birth_month, birth_year):
    current_date = datetime.now()
    current_year = current_date.year
    current_month = current_date.month
    current_day = current_date.day

    # Check if birthday has occurred this year
    if (current_month, current_day) < (birth_month, birth_day):
        age = current_year - birth_year - 1
    else:
        age = current_year - birth_year

    return age

# Get user input for birth date, month, and year
birth_day = int(input("Enter your birth day (1-31): "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_year = int(input("Enter your birth year: "))

# Validate input
if not (1 <= birth_day <= 31 and 1 <= birth_month <= 12):
    print("Invalid input for day or month.")
else:
    age = calculate_age(birth_day, birth_month, birth_year)
    print("Your age is:", age)'''



from datetime import datetime

def calculate_age(birth_day, birth_month, birth_year):
    current_date = datetime.now()
    current_year = current_date.year
    current_month = current_date.month
    current_day = current_date.day

    # Check if birthday has occurred this year
    if (current_month, current_day) < (birth_month, birth_day):
        age_year = current_year - birth_year - 1
    else:
        age_year = current_year - birth_year

    # Calculate remaining months and days
    if current_month < birth_month or (current_month == birth_month and current_day < birth_day):
        age_month = 12 - birth_month + current_month - 1
    else:
        age_month = current_month - birth_month

    # Calculate remaining days
    if current_day < birth_day:
        # Assuming all months have 30 days for simplicity
        age_day = 30 - birth_day + current_day
    else:
        age_day = current_day - birth_day

    return age_year, age_month, age_day

# Get user input for birth date, month, and year
birth_day = int(input("Enter your birth day (1-31): "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_year = int(input("Enter your birth year: "))

# Validate input
if not (1 <= birth_day <= 31 and 1 <= birth_month <= 12):
    print("Invalid input for day or month.")
else:
    age_year, age_month, age_day = calculate_age(birth_day, birth_month, birth_year)
    print("Your age is: {} years, {} months, and {} days.".format(age_year, age_month, age_day))

