"""
Python task
Mateusz Galganek
"""
from datetime import date
FILE_NAME = 'date.txt'


def date_type_detector(date_list):
    date_list = sorted(date_list)

    if len(str(date_list[2])) > 2:
        year = date_list[2]
    else:
        year = min(date_list)
    date_list.remove(year)

    month, day = date_list
    return day, month, year


def year_converter(year):
    year_len = len(str(year))
    if year_len == 2:
        full_year = int('20{}'.format(year))
    elif year_len == 1:
        full_year = int('200{}'.format(year))
    else:
        return year
    return full_year


def date_converter(input_date):
    result = 'is illegal'
    try:
        date_list = [int(number) for number in input_date.split('/')]
    except(ValueError):
        date_list = []

    if len(date_list) != 3:
        return result

    day, month, year = date_type_detector(date_list)
    year = year_converter(year)

    try:
        time = date(year, month, day)
    except(ValueError):
        pass
    else:
        result = time.isoformat()

    return result


def date_reader(input_file):
    try:
        date_file = open(input_file, 'r')
    except IOError:
        print('Could not open file!')
    else:
        for line in date_file.readlines():
            print(date_converter(line))
        date_file.close()


if __name__ == '__main__':
    date_reader(FILE_NAME)
