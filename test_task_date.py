"""
Testy do task_date.py
Mateusz Galganek
"""

from io import StringIO
from unittest import TestCase
import sys

from task_date import (
    date_converter,
    date_type_detector,
    year_converter,
    date_reader
)


class TestDate(TestCase):

    def test_date_type_detector(self):
        date_list = [
            [[31, 1, 5], (31, 5, 1)],
            [[2, 5, 31], (31, 5, 2)],
            [[5, 31, 2003], (31, 5, 2003)],
        ]
        for date_item in date_list:
            input_date = date_item[0]
            correct_result = date_item[1]
            result = date_type_detector(input_date)
            self.assertEqual(result, correct_result)

    def test_year_converter(self):
        years = [
            [2020, 2020],
            [20, 2020],
            [1, 2001]
        ]
        for year in years:
            input_date = year[0]
            correct_result = year[1]
            result = year_converter(input_date)
            self.assertEqual(result, correct_result)

    def test_date_reader_fail(self):
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            date_reader('no.txt')
            output = out.getvalue().strip()
            assert output == 'Could not open file!'
        finally:
            sys.stdout = saved_stdout

    def test_date_reader_success(self):
        FILE = 'test'
        f = open('test', 'w')
        f.write('12/11/10\n')
        f.close()
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            date_reader(FILE)
            output = out.getvalue().strip()
            assert output == '2010-11-12'
        finally:
            sys.stdout = saved_stdout

    def check_dates(self, dates):
        for date in dates:
            input_date = date[0]
            correct_result = date[1]
            result = date_converter(input_date)
            self.assertEqual(result, correct_result)

    def test_simple_legal_dates(self):
        dates = [
            ['12/11/10', '2010-11-12'],
            ['31/5/2012', '2012-05-31'],
            ['15/07/2011', '2011-07-15'],
        ]
        self.check_dates(dates)

    def test_legal_dates_combinations(self):
        dates = [
            ['22/12/10', '2010-12-22'],
            ['12/10/22', '2010-12-22'],
            ['10/22/12', '2010-12-22'],
        ]
        self.check_dates(dates)

    def test_legal_dates_years_types(self):
        dates = [
            ['31/5/0', '2000-05-31'],
            ['31/5/00', '2000-05-31'],
            ['31/5/2000', '2000-05-31'],
            ['31/5/1', '2001-05-31'],
            ['31/5/02', '2002-05-31'],
            ['31/5/2003', '2003-05-31'],
        ]
        self.check_dates(dates)

    def test_legal_dates_min_and_max(self):
        dates = [
            ['1/1/2000', '2000-01-01'],
            ['12/31/2999', '2999-12-31'],
        ]
        self.check_dates(dates)

    def test_illegal_data(self):
        dates = [
            ['1/11/99', 'is illegal'],
            ['1/40/11/3000', 'is illegal'],
            ['11/3000', 'is illegal'],
            ['12/40/22', 'is illegal'],
            ['/40/22', 'is illegal'],
            ['/40/', 'is illegal'],
            ['/', 'is illegal'],
        ]
        self.check_dates(dates)
