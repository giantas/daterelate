#! /usr/bin/env python3

import unittest
from testfixtures import compare
from daterelate.daterelate import relate
from datetime import datetime, timedelta


class TestRelateTestCase(unittest.TestCase):

    def setUp(self):
        self.now = datetime.now()

    @staticmethod
    def get_datetime(date_string):
        return datetime.strptime(date_string, '%d/%m/%Y')

    def test_compare_current_date(self):
        result = relate(self.now, self.now)
        expected_result = 'today'
        compare(result, expected_result)

    def test_compare_current_date_with_default(self):
        result = relate(self.now)
        expected_result = 'today'
        compare(result, expected_result)

    def test_compare_same_date(self):
        first_date = self.get_datetime('2/12/2018')
        second_date = self.get_datetime('02/12/2018')
        result = relate(second_date,
                           first_date, consider_now=False)
        expected_result = 'same day'

        compare(result, expected_result)

    def test_compare_date_after_today(self):
        second_date = self.now + timedelta(days=1)
        result = relate(second_date, self.now)
        expected_result = 'tomorrow'

        compare(result, expected_result)

    def test_compare_dates_in_succession(self):
        first_date = self.get_datetime('2/12/1950')
        later_date = self.get_datetime('3/12/1950')
        result = relate(later_date, first_date,
                           consider_now=False, future='after')
        expected_result = '1 day after'

        compare(result, expected_result)

    def test_compare_dates_in_succession_with_later_date_as_first(self):
        first_date = self.get_datetime('2/12/1950')
        later_date = self.get_datetime('3/12/1950')
        past = 'day before'
        result = relate(first_date, later_date, past=past)
        expected_result = 'yesterday'

        compare(result, expected_result)

    def test_compare_dates_in_succession_with_later_date_as_first_and_consider_now_as_false(self):
        first_date = self.get_datetime('2/12/1950')
        later_date = self.get_datetime('3/12/1950')
        result = relate(first_date, later_date,
                           past='before', consider_now=False)
        expected_result = '1 day before'

        compare(result, expected_result)


if __name__ == '__main__':
    unittest.main()
