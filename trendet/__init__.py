#!/usr/bin/env python

# Copyright 2018-2019 Alvaro Bartolome
# See LICENSE for details.

__author__ = 'Alvaro Bartolome @ alvarob96 on GitHub'
__version__ = '0.1'

from investpy import get_historical_data

from statistics import mean
import datetime
import string


def identify_trends(equity, from_date, to_date, window_size=5, trend_limit=3, labels=None):
    """
    This function retrieves historical data from the introduced `equity` from Investing
    via Web Scraping on the introduced date range. The resulting data can it either be
    stored in a :obj:`pandas.DataFrame` or in a :obj:`json` object with `ascending` or `descending` order.

    Args:
        equity (:obj:`str`): name of the equity to retrieve historical data from.
        from_date (:obj:`str`): date as `str` formatted as `dd/mm/yyyy`, from where data is going to be retrieved.
        to_date (:obj:`str`): date as `str` formatted as `dd/mm/yyyy`, until where data is going to be retrieved.
        window_size (:obj:`window`, optional): number of days from where market behaviour is considered a trend.
        trend_limit (:obj:`int`, optional): maximum number of trends to identify
        labels (:obj:`list`, optional): name of the labels for every identified trend.

    Returns:
        :obj:`pandas.DataFrame`:
            The function returns a :obj:`pandas.DataFrame` which contains the retrieved historical data from Investing
            using `investpy`, with a new column which identifies every trend found on the market between two dates
            identifying when did the trend started and when did it end. So the additional column contains labeled date
            ranges.
    Raises:
        ValueError: argument error.
    """

    if equity and not isinstance(equity, str):
        raise ValueError("equity argument needs to be a str.")

    if not equity:
        raise ValueError("equity parameter is mandatory and must be a valid equity name.")

    try:
        datetime.datetime.strptime(from_date, '%d/%m/%Y')
    except ValueError:
        raise ValueError("incorrect from_date date format, it should be 'dd/mm/yyyy'.")

    try:
        datetime.datetime.strptime(to_date, '%d/%m/%Y')
    except ValueError:
        raise ValueError("incorrect to_date format, it should be 'dd/mm/yyyy'.")

    start_date = datetime.datetime.strptime(from_date, '%d/%m/%Y')
    end_date = datetime.datetime.strptime(to_date, '%d/%m/%Y')

    if start_date >= end_date:
        raise ValueError("to_date should be greater than from_date, both formatted as 'dd/mm/yyyy'.")

    if not isinstance(window_size, int):
        raise ValueError('window_size must be an `int`')

    if isinstance(window_size, int) and window_size < 3:
        raise ValueError('window_size must be an `int` equal or higher than 3!')

    if not isinstance(trend_limit, int):
        raise ValueError('trend_limit must be an `int`')

    if isinstance(trend_limit, int) and trend_limit < 1:
        raise ValueError('trend_limit must be an `int` equal or higher than 1!')

    if labels is not None and isinstance(labels, list) and isinstance(trend_limit, int):
        if len(labels) != trend_limit:
            raise ValueError('if labels is not None and a `list`, it must have the same length as the trend_limit!')

    if labels is not None and not isinstance(labels, list):
        raise ValueError('labels is neither None or a `list`!')

    if labels is None:
        labels = [letter for letter in string.ascii_uppercase[:trend_limit]]

    try:
        df = get_historical_data(equity=str(equity),
                                 from_date=from_date,
                                 to_date=to_date,
                                 as_json=False,
                                 order='ascending',
                                 debug=False)
    except:
        raise RuntimeError('investpy function call failed!')

    limit = None
    values = list()

    trends = list()

    for index, value in enumerate(df['Close'], 0):
        if limit and limit > value:
            values.append(value)
            limit = mean(values)
        elif limit and limit < value:
            if len(values) > window_size:
                min_value = min(values)

                for counter, item in enumerate(values, 0):
                    if item == min_value:
                        break

                to_trend = from_trend + counter

                obj = {
                    'from': df.index.tolist()[from_trend],
                    'to': df.index.tolist()[to_trend],
                }

                trends.append(obj)

                if len(trends) >= trend_limit:
                    break

            limit = None
            values = list()
        else:
            from_trend = index

            values.append(value)
            limit = mean(values)

    for trend, label in zip(trends, labels):
        for index, row in df[trend['from']:trend['to']].iterrows():
            df.loc[index, 'Trend'] = label

    return df
