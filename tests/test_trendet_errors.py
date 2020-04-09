# Copyright 2019-2020 Alvaro Bartolome
# See LICENSE for details.

import pytest

from investpy import get_stock_historical_data

import trendet


def test_errors():
    """
    This function raises trendet errors to improve coverage
    """

    params = [
        {
            'stock': ['error'],
            'country': 'Spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 3,
            'labels': None,
            'identify': 'both',
        },
        {
            'stock': None,
            'country': 'Spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 3,
            'labels': None,
            'identify': 'both',
        },
        {
            'stock': 'error',
            'country': 'Spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 3,
            'labels': None,
            'identify': 'both',
        },
        {
            'stock': 'BBVA',
            'country': None,
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 3,
            'labels': None,
            'identify': 'both',
        },
        {
            'stock': 'BBVA',
            'country': 'error',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 3,
            'labels': None,
            'identify': 'both',
        },
        {
            'stock': 'BBVA',
            'country': ['error'],
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 3,
            'labels': None,
            'identify': 'both',
        },
        {
            'stock': 'BBVA',
            'country': 'Spain',
            'from_date': None,
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 3,
            'labels': None,
            'identify': 'both',
        },
        {
            'stock': 'BBVA',
            'country': 'Spain',
            'from_date': '01/01/2018',
            'to_date': None,
            'window_size': 5,
            'trend_limit': 3,
            'labels': None,
            'identify': 'both',
        },
        {
            'stock': 'BBVA',
            'country': 'Spain',
            'from_date': '01/01/2019',
            'to_date': '01/01/2018',
            'window_size': 5,
            'trend_limit': 3,
            'labels': None,
            'identify': 'both',
        },
        {
            'stock': 'BBVA',
            'country': 'Spain',
            'from_date': '01/01-2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 3,
            'labels': None,
            'identify': 'both',
        },
        {
            'stock': 'BBVA',
            'country': 'Spain',
            'from_date': '01/01/2018',
            'to_date': '_01*01/2019',
            'window_size': 5,
            'trend_limit': 3,
            'labels': None,
            'identify': 'both',
        },
        {
            'stock': 'BBVA',
            'country': 'Spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 0,
            'trend_limit': 3,
            'labels': None,
            'identify': 'both',
        },
        {
            'stock': 'BBVA',
            'country': 'Spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': -1,
            'labels': None,
            'identify': 'both',
        },
        {
            'stock': 'BBVA',
            'country': 'Spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': None,
            'labels': None,
            'identify': 'both',
        },
        {
            'stock': 'BBVA',
            'country': 'Spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': None,
            'trend_limit': 1,
            'labels': None,
            'identify': 'both',
        },
        {
            'stock': 'BBVA',
            'country': 'Spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 'error',
            'trend_limit': 1,
            'labels': None,
            'identify': 'both',
        },
        {
            'stock': 'BBVA',
            'country': 'Spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 1,
            'trend_limit': 'error',
            'labels': None,
            'identify': 'both',
        },
        {
            'stock': 'BBVA',
            'country': 'Spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 2,
            'trend_limit': 5,
            'labels': None,
            'identify': 'both',
        },
        {
            'stock': 'BBVA',
            'country': 'Spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 3,
            'labels': ['a', 'b'],
            'identify': 'both',
        },
        {
            'stock': 'BBVA',
            'country': 'Spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 3,
            'labels': 'error',
            'identify': 'both',
        },
        {
            'stock': 'BBVA',
            'country': 'Spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'window_size': 5,
            'trend_limit': 3,
            'labels': None,
            'identify': ['error'],
        },
        {
            'stock': 'BBVA',
            'country': 'Spain',
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
            trendet.identify_trends(stock=param['stock'],
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
            trendet.identify_all_trends(stock=param['stock'],
                                        country=param['country'],
                                        from_date=param['from_date'],
                                        to_date=param['to_date'],
                                        window_size=param['window_size'],
                                        identify=param['identify'])
        except:
            pass

    df = get_stock_historical_data(stock='REP',
                                   country='Spain',
                                   from_date='01/01/2018',
                                   to_date='01/01/2019')

    df['error'] = 'error'

    params = [
        {
            'df': None,
            'column': 'Close',
            'window_size': 5,
            'identify': 'both'
        },
        {
            'df': ['error'],
            'column': 'Close',
            'window_size': 5,
            'identify': 'both'
        },
        {
            'df': df,
            'column': None,
            'window_size': 5,
            'identify': 'both'
        },
        {
            'df': df,
            'column': ['error'],
            'window_size': 5,
            'identify': 'both'
        },
        {
            'df': df,
            'column': 'error',
            'window_size': 5,
            'identify': 'both'
        },
        {
            'df': df,
            'column': 'error',
            'window_size': 5,
            'identify': 'both'
        },
        {
            'df': df,
            'column': 'Close',
            'window_size': None,
            'identify': 'both'
        },
        {
            'df': df,
            'column': 'Close',
            'window_size': 1,
            'identify': 'both'
        },
        {
            'df': df,
            'column': 'Close',
            'window_size': 5,
            'identify': ['error']
        },
        {
            'df': df,
            'column': 'Close',
            'window_size': 5,
            'identify': 'error'
        },
    ]

    for param in params:
        try:
            trendet.identify_df_trends(df=param['df'],
                                       column=param['column'],
                                       window_size=param['window_size'],
                                       identify=param['identify'])
        except:
            pass


if __name__ == '__main__':
    test_errors()
