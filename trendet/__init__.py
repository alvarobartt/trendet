#!/usr/bin/env python

# Copyright 2018-2019 Alvaro Bartolome
# See LICENSE for details.

__author__ = 'Alvaro Bartolome @ alvarob96 on GitHub'
__version__ = '0.3'

from investpy import get_historical_data

import numpy as np

from statistics import mean
import datetime
import string


def identify_trends(equity, from_date, to_date, window_size=5, trend_limit=3, labels=None):
    """
    This function retrieves historical data from the introduced `equity` between two dates from Investing via investpy;
    and that data is later going to be analysed in order to detect/identify trends over a certain date range. A trend
    is considered so based on the window_size, which specifies the number of consecutive days which lead the algorithm
    to identify the market behaviour as a trend. So on, this function will identify both up and down trends and will
    remove the ones that overlap, keeping just the longer trend and discarding the nested trend; but it will just
    identify a maximum of trend_limit up and down trends which will be labeled as specified by labels list.

    Args:
        equity (:obj:`str`): name of the equity to retrieve historical data from.
        from_date (:obj:`str`): date as `str` formatted as `dd/mm/yyyy`, from where data is going to be retrieved.
        to_date (:obj:`str`): date as `str` formatted as `dd/mm/yyyy`, until where data is going to be retrieved.
        window_size (:obj:`window`, optional): number of days from where market behaviour is considered a trend.
        trend_limit (:obj:`int`, optional): maximum number of trends to identify
        labels (:obj:`list`, optional): name of the labels for every identified trend.

    Returns:
        :obj:`pandas.DataFrame`:
            :obj:`pandas.DataFrame`:
            The function returns a :obj:`pandas.DataFrame` which contains the retrieved historical data from Investing
            using `investpy`, with a new column which identifies every trend found on the market between two dates
            identifying when did the trend started and when did it end. So the additional column contains labeled date
            ranges, representing both bullish (up) and bearish (down) trends.
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

    try:
        df = get_historical_data(equity=str(equity),
                                 from_date=from_date,
                                 to_date=to_date,
                                 as_json=False,
                                 order='ascending',
                                 debug=False)
    except:
        raise RuntimeError('investpy function call failed!')

    objs = list()

    up_trend = {
        'name': 'Up Trend',
        'element': np.negative(df['Close'])
    }

    objs.append(up_trend)

    down_trend = {
        'name': 'Down Trend',
        'element': df['Close']
    }

    objs.append(down_trend)

    results = dict()

    for obj in objs:
        limit = None
        values = list()

        trends = list()

        for index, value in enumerate(obj['element'], 0):
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

                    trend = {
                        'from': df.index.tolist()[from_trend],
                        'to': df.index.tolist()[to_trend],
                    }

                    trends.append(trend)

                limit = None
                values = list()
            else:
                from_trend = index

                values.append(value)
                limit = mean(values)

        results[obj['name']] = trends

    up_trends = list()
    down_trends = list()

    for up in results['Up Trend']:
        flag = True

        for down in results['Down Trend']:
            if down['from'] < up['from'] < down['to'] or down['from'] < up['to'] < down['to']:
                if (up['to'] - up['from']).days > (down['to'] - down['from']).days:
                    flag = True
                else:
                    flag = False
            else:
                flag = True

        if flag is True:
            up_trends.append(up)

    if labels is None:
        up_labels = [letter for letter in string.ascii_uppercase[:len(up_trends)]]
    else:
        up_labels = labels

    for up_trend, up_label in zip(up_trends, up_labels):
        for index, row in df[up_trend['from']:up_trend['to']].iterrows():
            df.loc[index, 'Up Trend'] = up_label

    for down in results['Down Trend']:
        flag = True

        for up in results['Up Trend']:
            if up['from'] < down['from'] < up['to'] or up['from'] < down['to'] < up['to']:
                if (up['to'] - up['from']).days < (down['to'] - down['from']).days:
                    flag = True
                else:
                    flag = False
            else:
                flag = True

        if flag is True:
            down_trends.append(down)

    if labels is None:
        down_labels = [letter for letter in string.ascii_uppercase[:len(down_trends)]]
    else:
        down_labels = labels

    for down_trend, down_label in zip(down_trends, down_labels):
        for index, row in df[down_trend['from']:down_trend['to']].iterrows():
            df.loc[index, 'Down Trend'] = down_label

    return df


def identify_all_trends(equity, from_date, to_date, window_size=5):
    """
    This function retrieves historical data from the introduced `equity` between two dates from Investing via investpy;
    and that data is later going to be analysed in order to detect/identify trends over a certain date range. A trend
    is considered so based on the window_size, which specifies the number of consecutive days which lead the algorithm
    to identify the market behaviour as a trend. So on, this function will identify both up and down trends and will
    remove the ones that overlap, keeping just the longer trend and discarding the nested trend.

    Args:
        equity (:obj:`str`): name of the equity to retrieve historical data from.
        from_date (:obj:`str`): date as `str` formatted as `dd/mm/yyyy`, from where data is going to be retrieved.
        to_date (:obj:`str`): date as `str` formatted as `dd/mm/yyyy`, until where data is going to be retrieved.
        window_size (:obj:`window`, optional): number of days from where market behaviour is considered a trend.

    Returns:
        :obj:`pandas.DataFrame`:
            The function returns a :obj:`pandas.DataFrame` which contains the retrieved historical data from Investing
            using `investpy`, with a new column which identifies every trend found on the market between two dates
            identifying when did the trend started and when did it end. So the additional column contains labeled date
            ranges, representing both bullish (up) and bearish (down) trends.
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

    try:
        df = get_historical_data(equity=str(equity),
                                 from_date=from_date,
                                 to_date=to_date,
                                 as_json=False,
                                 order='ascending',
                                 debug=False)
    except:
        raise RuntimeError('investpy function call failed!')

    objs = list()

    up_trends = {
        'name': 'Up Trend',
        'element': np.negative(df['Close'])
    }

    objs.append(up_trends)

    down_trends = {
        'name': 'Down Trend',
        'element': df['Close']
    }

    objs.append(down_trends)

    results = dict()

    for obj in objs:
        limit = None
        values = list()

        trends = list()

        for index, value in enumerate(obj['element'], 0):
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

                    trend = {
                        'from': df.index.tolist()[from_trend],
                        'to': df.index.tolist()[to_trend],
                    }

                    trends.append(trend)

                limit = None
                values = list()
            else:
                from_trend = index

                values.append(value)
                limit = mean(values)

        results[obj['name']] = trends

    up_trends = list()
    down_trends = list()

    for up in results['Up Trend']:
        flag = True

        for down in results['Down Trend']:
            if down['from'] < up['from'] < down['to'] or down['from'] < up['to'] < down['to']:
                if (up['to'] - up['from']).days > (down['to'] - down['from']).days:
                    flag = True
                else:
                    flag = False
            else:
                flag = True

        if flag is True:
            up_trends.append(up)

    labels = [letter for letter in string.ascii_uppercase[:len(up_trends)]]

    for up_trend, label in zip(up_trends, labels):
        for index, row in df[up_trend['from']:up_trend['to']].iterrows():
            df.loc[index, 'Up Trend'] = label

    for down in results['Down Trend']:
        flag = True

        for up in results['Up Trend']:
            if up['from'] < down['from'] < up['to'] or up['from'] < down['to'] < up['to']:
                if (up['to'] - up['from']).days < (down['to'] - down['from']).days:
                    flag = True
                else:
                    flag = False
            else:
                flag = True

        if flag is True:
            down_trends.append(down)

    labels = [letter for letter in string.ascii_uppercase[:len(down_trends)]]

    for down_trend, label in zip(down_trends, labels):
        for index, row in df[down_trend['from']:down_trend['to']].iterrows():
            df.loc[index, 'Down Trend'] = label

    return df
