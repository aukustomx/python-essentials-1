MONTHS_LENGTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if month >= 1 and month <= 12:
        if month != 2:
            return MONTHS_LENGTH[month - 1]
        else:
            is_leap = is_year_leap(year)
            if is_leap:
                return 29
            else:
                return 28


def day_of_year(year, month, day):
    copy_months_length = MONTHS_LENGTH[:]
    
    if is_year_leap(year):
        copy_months_length[1] = 29
    
    days = 0
    for month in range(0, month - 1):
        days += copy_months_length[month]
    
    days += day
    return days


print(day_of_year(2000, 12, 31))
print(day_of_year(2000, 3, 1))
