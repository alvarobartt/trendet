#!/usr/bin/env python

# Copyright 2018-2019 Alvaro Bartolome
# See LICENSE for details.

import pytest

import trendet


def test_errors():
    """
    This function raises trendet errors to improve coverage
    """

    print(trendet.__author__)
    print(trendet.__version__)

    params = [
        {
            'equity': ['error'],
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 1,
            'trend_limit': 3,
            'labels': None,
        },
        {
            'equity': None,
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 1,
            'trend_limit': 3,
            'labels': None,
        },
        {
            'equity': 'error',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 3,
            'labels': None,
        },
        {
            'equity': 'bbva',
            'from_date': None,
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 3,
            'labels': None,
        },
        {
            'equity': 'bbva',
            'from_date': '01/01/2018',
            'to_date': None,
            'window_size': 5,
            'trend_limit': 3,
            'labels': None,
        },
        {
            'equity': 'bbva',
            'from_date': '01/01/2019',
            'to_date': '01/01/2018',
            'window_size': 5,
            'trend_limit': 3,
            'labels': None,
        },
        {
            'equity': 'bbva',
            'from_date': '01/01-2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 3,
            'labels': None,
        },
        {
            'equity': 'bbva',
            'from_date': '01/01-2018',
            'to_date': '_01*01/2019',
            'window_size': 5,
            'trend_limit': 3,
            'labels': None,
        },
        {
            'equity': 'bbva',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 0,
            'trend_limit': 3,
            'labels': None,
        },
        {
            'equity': 'bbva',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': -1,
            'labels': None,
        },
        {
            'equity': 'bbva',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': None,
            'labels': None,
        },
        {
            'equity': 'bbva',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': None,
            'trend_limit': 1,
            'labels': None,
        },
        {
            'equity': 'bbva',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 'error',
            'trend_limit': 1,
            'labels': None,
        },
        {
            'equity': 'bbva',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 1,
            'trend_limit': 'error',
            'labels': None,
        },
        {
            'equity': 'bbva',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 2,
            'trend_limit': 5,
            'labels': None,
        },
        {
            'equity': 'bbva',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 3,
            'labels': ['a', 'b'],
        },
        {
            'equity': 'bbva',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 3,
            'labels': 'error',
        },
    ]

    for param in params:
        try:
            trendet.identify_trends(equity=param['equity'],
                                    from_date=param['from_date'],
                                    to_date=param['to_date'],
                                    window_size=param['window_size'],
                                    trend_limit=param['trend_limit'],
                                    labels=param['labels'])
        except:
            continue


if __name__ == '__main__':
    test_errors()