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


def read_file(file_name):
    dates = []
    with open(file_name, 'r') as file:
        for line in file:
            date = format_date(line.strip())
            if date:
                dates.append(date)
    return dates


def write_to_file(input_file_name, output_file_name):
    dates = read_file(input_file_name)

    with open(output_file_name, 'w') as output_file:
        for date in dates:
            output_file.write(date + '\n')


if __name__ == '__main__':
    file_name = "inputDates.txt"
    dates_from_file = read_file(file_name)
    print("\nDates from file:")
    for date in dates_from_file:
        print(date)
    output_file = "parsedDates.txt"
    write_to_file(file_name, output_file)

    print("\nParsed dates written to 'parsedDates.txt'")
    
