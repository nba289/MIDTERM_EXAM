def days(birthday):
    birth_year = int(birthday.split("-")[2])
    current_year = 2024
    years_since_birth = current_year - birth_year - 1
    total_days = 0
    for year in range(birth_year + 1, current_year):
        if year % 4 == 0:
            total_days += 366
        else:
            total_days += 365
    return total_days

birthday = "28-09-2004"
print("Days since you were born:", days(birthday))
