#! /usr/bin/env python3

import unittest

from datetime import datetime

from testfixtures import compare

from daterelate.daterelate import relate_from_string


class TestRelateFromStringTestCase(unittest.TestCase):

    def setUp(self):
        self.now = datetime.now()

    def test_compare_same_date(self):
        first_date = '2/12/2018'
        second_date = '2 December 2018'
        result = relate_from_string(second_date,
                        first_date, consider_now=False)
        expected_result = 'same day'

        compare(result, expected_result)

    def test_compare_date_in_words(self):
        first_date = 'February 11, 2018'
        second_date = 'Wednesday 7, 2018 February'
        result = relate_from_string(second_date, first_date)
        expected_result = '4 days ago'

        compare(result, expected_result)

    def test_compare_dates_in_succession(self):
        first_date = '2/12/1950'
        later_date = '3/12/1950'
        result = relate_from_string(later_date, first_date,
                        consider_now=False, future='after')
        expected_result = '1 day after'

        compare(result, expected_result)

    def test_compare_dates_in_succession_with_later_date_as_first(self):
        first_date = '2/12/1950'
        later_date = '3/12/1950'
        past = 'day before'
        result = relate_from_string(first_date, later_date, past=past)
        expected_result = 'yesterday'

        compare(result, expected_result)

    def test_compare_dates_in_succession_with_later_date_as_first_and_consider_now_as_false(self):
        first_date = '2/12/1950'
        later_date = '3/12/1950'
        result = relate_from_string(first_date, later_date,
                        past='before', consider_now=False)
        expected_result = '1 day before'

        compare(result, expected_result)


if __name__ == '__main__':
    unittest.main()
