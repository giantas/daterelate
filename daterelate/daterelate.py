#! /usr/bin/env python3

from datetime import datetime

from dateutil import parser


def _check_same_date(first_date, later_date, consider_now, same_day):
    if first_date == later_date:
        if consider_now:
            return 'today'
        else:
            return same_day
    else:
        return False


def _evaluate_day_difference(days, future, past, consider_now):
    absolute_days = abs(days)
    if days == 1:
        if consider_now or 'tomorrow' in future.lower():
            string = 'tomorrow'

        else:
            string = '{} day {}'.format(absolute_days, future)

    elif days == -1:
        if consider_now or 'yesterday' in past.lower():
            string = 'yesterday'

        else:
            string = '{} day {}'.format(absolute_days, past)

    elif days > 0:
        string = '{} days {}'.format(absolute_days, future)

    elif days < -1:
        string = '{} days {}'.format(absolute_days, past)

    else:
        raise ValueError('days could not be evaluated')

    return string


def relate(later_date, first_date=datetime.now(),
           same_day='same day', future='to come',
           past='prior', consider_now=True):
    """Takes in 2 datetime objects and relates
    later_date to first_date"""

    first_date = first_date.date()
    later_date = later_date.date()

    is_same_date = _check_same_date(first_date, later_date,
                                    consider_now, same_day)
    if is_same_date:
        return is_same_date

    days = (later_date - first_date).days

    return _evaluate_day_difference(
        days, future=future, past=past, consider_now=consider_now)


def relate_from_string(later_date, first_date=datetime.now(),
                       future='to come', same_day='same day',
                       past='ago', consider_now=True, **kwargs):
    """Takes in 2 strings of dates and compares
    later_date in relation to first_date"""

    day_first = kwargs.pop('dayfirst', True)

    first_date = parser.parse(
        first_date, dayfirst=day_first, **kwargs)
    later_date = parser.parse(
        later_date, dayfirst=day_first, **kwargs)

    return relate(later_date, first_date=first_date,
                  same_day=same_day, future=future,
                  past=past, consider_now=consider_now)
