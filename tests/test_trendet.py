#!/usr/bin/env python

# Copyright 2018-2019 Alvaro Bartolome
# See LICENSE for details.

import pytest

import trendet


def test_trendet():
    """
    This function checks that main functions of trendet work properly.
    """

    print(trendet.__author__)
    print(trendet.__version__)

    params = [
        {
            'equity': 'bbva',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 3,
            'labels': None,
        },
    ]

    for param in params:
        trendet.identify_trends(equity=param['equity'],
                                from_date=param['from_date'],
                                to_date=param['to_date'],
                                window_size=param['window_size'],
                                trend_limit=param['trend_limit'],
                                labels=param['labels'])


if __name__ == '__main__':
    test_trendet()