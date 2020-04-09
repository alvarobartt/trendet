# Copyright 2019-2020 Alvaro Bartolome
# See LICENSE for details.

import pytest

from investpy import get_stock_historical_data, get_stocks_list

import trendet


def test_trendet():
    """
    This function checks that main functions of trendet work properly.
    """

    print(trendet.__author__)
    print(trendet.__version__)

    params = [
        {
            'stock': 'BBVA',
            'country': 'Spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 2,
            'labels': ['A', 'B'],
            'identify': 'both'
        },
        {
            'stock': 'BBVA',
            'country': 'Spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 2,
            'labels': None,
            'identify': 'up',
        },
        {
            'stock': 'BBVA',
            'country': 'Spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 2,
            'labels': ['A', 'B'],
            'identify': 'up',
        },
        {
            'stock': 'BBVA',
            'country': 'Spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 2,
            'labels': ['A', 'B'],
            'identify': 'down',
        },
        {
            'stock': 'BBVA',
            'country': 'Spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 2,
            'labels': None,
            'identify': 'down',
        }
    ]

    stocks = get_stocks_list(country='Spain')

    for stock in stocks[:25]:
        obj = {
            'stock': stock,
            'country': 'Spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 5,
            'labels': None,
            'identify': 'both',
        }

        params.append(obj)

    for param in params:
        trendet.identify_trends(stock=param['stock'],
                                country=param['country'],
                                from_date=param['from_date'],
                                to_date=param['to_date'],
                                window_size=param['window_size'],
                                trend_limit=param['trend_limit'],
                                labels=param['labels'],
                                identify=param['identify'])

        trendet.identify_all_trends(stock=param['stock'],
                                    country=param['country'],
                                    from_date=param['from_date'],
                                    to_date=param['to_date'],
                                    window_size=param['window_size'],
                                    identify=param['identify'])

    df = get_stock_historical_data(stock='REP',
                                   country='Spain',
                                   from_date='01/01/2018',
                                   to_date='01/01/2019')

    params = [
        {
            'column': 'Close',
            'window_size': 5,
            'identify': 'both'
        },
        {
            'column': 'Close',
            'window_size': 5,
            'identify': 'up'
        },
        {
            'column': 'Close',
            'window_size': 5,
            'identify': 'down'
        },
    ]

    for param in params:
        trendet.identify_df_trends(df=df,
                                   column=param['column'],
                                   window_size=param['window_size'],
                                   identify=param['identify'])


if __name__ == '__main__':
    test_trendet()
