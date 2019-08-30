#!/usr/bin/env python

# Copyright 2018-2019 Alvaro Bartolome
# See LICENSE for details.

import pytest

import trendet
import investpy


def test_trendet():
    """
    This function checks that main functions of trendet work properly.
    """

    author = trendet.__author__
    print(author)
    version = trendet.__version__
    print(version)

    equities = investpy.get_equities_list()

    params = list()

    for equity in equities[:15]:
        obj = {
            'equity': equity,
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 5,
            'labels': None,
            'identify': 'both',
        }

        params.append(obj)

    obj = {
        'equity': 'bbva',
        'from_date': '01/01/2018',
        'to_date': '01/01/2019',
        'window_size': 5,
        'trend_limit': 2,
        'labels': ['A', 'B'],
        'identify': 'both'
    }

    params.append(obj)

    obj = {
        'equity': 'bbva',
        'from_date': '01/01/2018',
        'to_date': '01/01/2019',
        'window_size': 5,
        'trend_limit': 2,
        'labels': None,
        'identify': 'up',
    }

    params.append(obj)

    obj = {
        'equity': 'bbva',
        'from_date': '01/01/2018',
        'to_date': '01/01/2019',
        'window_size': 5,
        'trend_limit': 2,
        'labels': ['A', 'B'],
        'identify': 'up',
    }

    params.append(obj)

    obj = {
        'equity': 'bbva',
        'from_date': '01/01/2018',
        'to_date': '01/01/2019',
        'window_size': 5,
        'trend_limit': 2,
        'labels': None,
        'identify': 'down',
    }

    params.append(obj)

    obj = {
        'equity': 'bbva',
        'from_date': '01/01/2018',
        'to_date': '01/01/2019',
        'window_size': 5,
        'trend_limit': 2,
        'labels': ['A', 'B'],
        'identify': 'down',
    }

    params.append(obj)

    for param in params:
        trendet.identify_trends(equity=param['equity'],
                                from_date=param['from_date'],
                                to_date=param['to_date'],
                                window_size=param['window_size'],
                                trend_limit=param['trend_limit'],
                                labels=param['labels'],
                                identify=param['identify'])

        trendet.identify_all_trends(equity=param['equity'],
                                    from_date=param['from_date'],
                                    to_date=param['to_date'],
                                    window_size=param['window_size'],
                                    identify=param['identify'])


if __name__ == '__main__':
    test_trendet()
