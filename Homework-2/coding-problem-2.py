# Prabhu Roka
# 1986444
import datetime


def format_date(date_string):
    try:
        date_object = datetime.datetime.strptime(date_string, '%B %d, %Y')
        current_date = datetime.datetime.now()
        if date_object <= current_date:
            return date_object.strftime('%-m/%-d/%Y')
    except ValueError:
        pass

    return None


if __name__ == '__main__':
    input_dates = []
    date = input().strip()
    formatted_date = format_date(date)
    if formatted_date:
       input_dates.append(formatted_date)

    for date in input_dates:
        print(date)
