#!/usr/bin/env python

# Copyright 2018-2019 Alvaro Bartolome
# See LICENSE for details.

import pytest

import trendet


def test_errors():
    """
    This function raises trendet errors to improve coverage
    """

    params = [
        {
            'equity': ['error'],
            'country': 'spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 3,
            'labels': None,
            'identify': 'both',
        },
        {
            'equity': None,
            'country': 'spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 3,
            'labels': None,
            'identify': 'both',
        },
        {
            'equity': 'error',
            'country': 'spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 3,
            'labels': None,
            'identify': 'both',
        },
        {
            'equity': 'bbva',
            'country': None,
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 3,
            'labels': None,
            'identify': 'both',
        },
        {
            'equity': 'bbva',
            'country': 'error',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 3,
            'labels': None,
            'identify': 'both',
        },
        {
            'equity': 'bbva',
            'country': ['error'],
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 3,
            'labels': None,
            'identify': 'both',
        },
        {
            'equity': 'bbva',
            'country': 'spain',
            'from_date': None,
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 3,
            'labels': None,
            'identify': 'both',
        },
        {
            'equity': 'bbva',
            'country': 'spain',
            'from_date': '01/01/2018',
            'to_date': None,
            'window_size': 5,
            'trend_limit': 3,
            'labels': None,
            'identify': 'both',
        },
        {
            'equity': 'bbva',
            'country': 'spain',
            'from_date': '01/01/2019',
            'to_date': '01/01/2018',
            'window_size': 5,
            'trend_limit': 3,
            'labels': None,
            'identify': 'both',
        },
        {
            'equity': 'bbva',
            'country': 'spain',
            'from_date': '01/01-2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 3,
            'labels': None,
            'identify': 'both',
        },
        {
            'equity': 'bbva',
            'country': 'spain',
            'from_date': '01/01/2018',
            'to_date': '_01*01/2019',
            'window_size': 5,
            'trend_limit': 3,
            'labels': None,
            'identify': 'both',
        },
        {
            'equity': 'bbva',
            'country': 'spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 0,
            'trend_limit': 3,
            'labels': None,
            'identify': 'both',
        },
        {
            'equity': 'bbva',
            'country': 'spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': -1,
            'labels': None,
            'identify': 'both',
        },
        {
            'equity': 'bbva',
            'country': 'spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': None,
            'labels': None,
            'identify': 'both',
        },
        {
            'equity': 'bbva',
            'country': 'spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': None,
            'trend_limit': 1,
            'labels': None,
            'identify': 'both',
        },
        {
            'equity': 'bbva',
            'country': 'spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 'error',
            'trend_limit': 1,
            'labels': None,
            'identify': 'both',
        },
        {
            'equity': 'bbva',
            'country': 'spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 1,
            'trend_limit': 'error',
            'labels': None,
            'identify': 'both',
        },
        {
            'equity': 'bbva',
            'country': 'spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 2,
            'trend_limit': 5,
            'labels': None,
            'identify': 'both',
        },
        {
            'equity': 'bbva',
            'country': 'spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 3,
            'labels': ['a', 'b'],
            'identify': 'both',
        },
        {
            'equity': 'bbva',
            'country': 'spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 3,
            'labels': 'error',
            'identify': 'both',
        },
        {
            'equity': 'bbva',
            'country': 'spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 3,
            'labels': None,
            'identify': ['error'],
        },
        {
            'equity': 'bbva',
            'country': 'spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 3,
            'labels': None,
            'identify': 'error',
        },
    ]

    for param in params:
        try:
            trendet.identify_trends(equity=param['equity'],
                                    country=param['country'],
                                    from_date=param['from_date'],
                                    to_date=param['to_date'],
                                    window_size=param['window_size'],
                                    trend_limit=param['trend_limit'],
                                    labels=param['labels'],
                                    identify=param['identify'])
        except:
            pass

        try:
            trendet.identify_all_trends(equity=param['equity'],
                                        country=param['country'],
                                        from_date=param['from_date'],
                                        to_date=param['to_date'],
                                        window_size=param['window_size'],
                                        identify=param['identify'])
        except:
            pass


if __name__ == '__main__':
    test_errors()
