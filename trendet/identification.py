# Copyright 2019-2020 Alvaro Bartolome
# See LICENSE for details.

from investpy import get_stock_historical_data

import numpy as np
import pandas as pd

from statistics import mean

from unidecode import unidecode

import datetime
import string


def identify_trends(stock, country, from_date, to_date, window_size=5, trend_limit=3, labels=None, identify='both'):
    """
    This function retrieves historical data from the introduced `stock` between two dates from Investing via investpy;
    and that data is later going to be analysed in order to detect/identify trends over a certain date range. A trend
    is considered so based on the window_size, which specifies the number of consecutive days which lead the algorithm
    to identify the market behaviour as a trend. So on, this function will identify both up and down trends and will
    remove the ones that overlap, keeping just the longer trend and discarding the nested trend; but it will just
    identify a maximum of trend_limit up and down trends which will be labeled as specified by labels list.

    Args:
        stock (:obj:`str`): symbol of the stock to retrieve historical data from.
        country (:obj:`str`): name of the country from where the stock is.
        from_date (:obj:`str`): date as `str` formatted as `dd/mm/yyyy`, from where data is going to be retrieved.
        to_date (:obj:`str`): date as `str` formatted as `dd/mm/yyyy`, until where data is going to be retrieved.
        window_size (:obj:`window`, optional): number of days from where market behaviour is considered a trend.
        trend_limit (:obj:`int`, optional): maximum number of trends to identify
        labels (:obj:`list`, optional): name of the labels for every identified trend.
        identify (:obj:`str`, optional):
            which trends does the user wants to be identified, it can either be 'both', 'up' or 'down'.

    Returns:
        :obj:`pandas.DataFrame`:
            The function returns a :obj:`pandas.DataFrame` which contains the retrieved historical data from Investing
            using `investpy`, with a new column which identifies every trend found on the market between two dates
            identifying when did the trend started and when did it end. So the additional column contains labeled date
            ranges, representing both bullish (up) and bearish (down) trends.

    Raises:
        ValueError: raised if any of the introduced arguments errored.
    """

    if stock and not isinstance(stock, str):
        raise ValueError("stock argument needs to be a `str`.")

    if not stock:
        raise ValueError("stock parameter is mandatory and must be a valid stock symbol.")

    stock = unidecode(stock.strip().lower())

    if not country:
        raise ValueError("country parameter is mandatory and must be a valid country name as listed in "
                         "`investpy.get_stock_countries()`.")

    if country and not isinstance(country, str):
        raise ValueError("country argument is mandatory and needs to be a `str`.")

    country = unidecode(country.strip().lower())

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

    if not isinstance(identify, str):
        raise ValueError('identify should be a `str` contained in [both, up, down]!')

    if isinstance(identify, str) and identify not in ['both', 'up', 'down']:
        raise ValueError('identify should be a `str` contained in [both, up, down]!')

    try:
        df = get_stock_historical_data(stock=stock,
                                       country=country,
                                       from_date=from_date,
                                       to_date=to_date)
    except Exception as e:
        raise RuntimeError(f'investpy function call failed with Exception: {e}!')

    objs = list()

    up_trend = {
        'name': 'Up Trend',
        'element': np.negative(df['Close'])
    }

    down_trend = {
        'name': 'Down Trend',
        'element': df['Close']
    }

    if identify == 'both':
        objs.append(up_trend)
        objs.append(down_trend)
    elif identify == 'up':
        objs.append(up_trend)
    elif identify == 'down':
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

    if identify == 'both':
        up_trends = list()

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

        down_trends = list()

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
    elif identify == 'up':
        up_trends = results['Up Trend']

        if labels is None:
            up_labels = [letter for letter in string.ascii_uppercase[:len(up_trends)]]
        else:
            up_labels = labels

        for up_trend, up_label in zip(up_trends, up_labels):
            for index, row in df[up_trend['from']:up_trend['to']].iterrows():
                df.loc[index, 'Up Trend'] = up_label

        return df
    elif identify == 'down':
        down_trends = results['Down Trend']

        if labels is None:
            down_labels = [letter for letter in string.ascii_uppercase[:len(down_trends)]]
        else:
            down_labels = labels

        for down_trend, down_label in zip(down_trends, down_labels):
            for index, row in df[down_trend['from']:down_trend['to']].iterrows():
                df.loc[index, 'Down Trend'] = down_label

        return df


def identify_all_trends(stock, country, from_date, to_date, window_size=5, identify='both'):
    """
    This function retrieves historical data from the introduced `stock` between two dates from Investing via investpy;
    and that data is later going to be analysed in order to detect/identify trends over a certain date range. A trend
    is considered so based on the window_size, which specifies the number of consecutive days which lead the algorithm
    to identify the market behaviour as a trend. So on, this function will identify both up and down trends and will
    remove the ones that overlap, keeping just the longer trend and discarding the nested trend.

    Args:
        stock (:obj:`str`): symbol of the stock to retrieve historical data from.
        country (:obj:`str`): name of the country from where the stock is.
        from_date (:obj:`str`): date as `str` formatted as `dd/mm/yyyy`, from where data is going to be retrieved.
        to_date (:obj:`str`): date as `str` formatted as `dd/mm/yyyy`, until where data is going to be retrieved.
        window_size (:obj:`window`, optional): number of days from where market behaviour is considered a trend.
        identify (:obj:`str`, optional):
            which trends does the user wants to be identified, it can either be 'both', 'up' or 'down'.

    Returns:
        :obj:`pandas.DataFrame`:
            The function returns a :obj:`pandas.DataFrame` which contains the retrieved historical data from Investing
            using `investpy`, with a new column which identifies every trend found on the market between two dates
            identifying when did the trend started and when did it end. So the additional column contains labeled date
            ranges, representing both bullish (up) and bearish (down) trends.

    Raises:
        ValueError: raised if any of the introduced arguments errored.
    """

    if stock and not isinstance(stock, str):
        raise ValueError("stock argument needs to be a `str`.")

    if not stock:
        raise ValueError("stock parameter is mandatory and must be a valid stock symbol.")

    stock = unidecode(stock.strip().lower())

    if not country:
        raise ValueError("country parameter is mandatory and must be a valid country name as listed in "
                         "`investpy.get_stock_countries()`.")

    if country and not isinstance(country, str):
        raise ValueError("country argument is mandatory and needs to be a `str`.")

    country = unidecode(country.strip().lower())

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

    if not isinstance(identify, str):
        raise ValueError('identify should be a `str` contained in [both, up, down]!')

    if isinstance(identify, str) and identify not in ['both', 'up', 'down']:
        raise ValueError('identify should be a `str` contained in [both, up, down]!')

    try:
        df = get_stock_historical_data(stock=stock,
                                       country=country,
                                       from_date=from_date,
                                       to_date=to_date)
    except Exception as e:
        raise RuntimeError(f'investpy function call failed with Exception: {e}!')

    objs = list()

    up_trend = {
        'name': 'Up Trend',
        'element': np.negative(df['Close'])
    }

    down_trend = {
        'name': 'Down Trend',
        'element': df['Close']
    }

    if identify == 'both':
        objs.append(up_trend)
        objs.append(down_trend)
    elif identify == 'up':
        objs.append(up_trend)
    elif identify == 'down':
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

    if identify == 'both':
        up_trends = list()

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

        down_trends = list()

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
    elif identify == 'up':
        up_trends = results['Up Trend']

        up_labels = [letter for letter in string.ascii_uppercase[:len(up_trends)]]

        for up_trend, up_label in zip(up_trends, up_labels):
            for index, row in df[up_trend['from']:up_trend['to']].iterrows():
                df.loc[index, 'Up Trend'] = up_label

        return df
    elif identify == 'down':
        down_trends = results['Down Trend']

        down_labels = [letter for letter in string.ascii_uppercase[:len(down_trends)]]

        for down_trend, down_label in zip(down_trends, down_labels):
            for index, row in df[down_trend['from']:down_trend['to']].iterrows():
                df.loc[index, 'Down Trend'] = down_label

        return df


def identify_df_trends(df, column, window_size=5, identify='both'):
    """
    This function receives as input a pandas.DataFrame from which data is going to be analysed in order to
    detect/identify trends over a certain date range. A trend is considered so based on the window_size, which
    specifies the number of consecutive days which lead the algorithm to identify the market behaviour as a trend. So
    on, this function will identify both up and down trends and will remove the ones that overlap, keeping just the
    longer trend and discarding the nested trend.

    Args:
        df (:obj:`pandas.DataFrame`): dataframe containing the data to be analysed.
        column (:obj:`str`): name of the column from where trends are going to be identified.
        window_size (:obj:`window`, optional): number of days from where market behaviour is considered a trend.
        identify (:obj:`str`, optional):
            which trends does the user wants to be identified, it can either be 'both', 'up' or 'down'.

    Returns:
        :obj:`pandas.DataFrame`:
            The function returns a :obj:`pandas.DataFrame` which contains the retrieved historical data from Investing
            using `investpy`, with a new column which identifies every trend found on the market between two dates
            identifying when did the trend started and when did it end. So the additional column contains labeled date
            ranges, representing both bullish (up) and bearish (down) trends.
    Raises:
        ValueError: raised if any of the introduced arguments errored.
    """

    if df is None:
        raise ValueError("df argument is mandatory and needs to be a `pandas.DataFrame`.")

    if not isinstance(df, pd.DataFrame):
        raise ValueError("df argument is mandatory and needs to be a `pandas.DataFrame`.")

    if column is None:
        raise ValueError("column parameter is mandatory and must be a valid column name.")

    if column and not isinstance(column, str):
        raise ValueError("column argument needs to be a `str`.")

    if isinstance(df, pd.DataFrame):
        if column not in df.columns:
            raise ValueError("introduced column does not match any column from the specified `pandas.DataFrame`.")
        else:
            if df[column].dtype not in ['int64', 'float64']:
                raise ValueError("supported values are just `int` or `float`, and the specified column of the "
                                 "introduced `pandas.DataFrame` is " + str(df[column].dtype))

    if not isinstance(window_size, int):
        raise ValueError('window_size must be an `int`')

    if isinstance(window_size, int) and window_size < 3:
        raise ValueError('window_size must be an `int` equal or higher than 3!')

    if not isinstance(identify, str):
        raise ValueError('identify should be a `str` contained in [both, up, down]!')

    if isinstance(identify, str) and identify not in ['both', 'up', 'down']:
        raise ValueError('identify should be a `str` contained in [both, up, down]!')

    objs = list()

    up_trend = {
        'name': 'Up Trend',
        'element': np.negative(df[column])
    }

    down_trend = {
        'name': 'Down Trend',
        'element': df[column]
    }

    if identify == 'both':
        objs.append(up_trend)
        objs.append(down_trend)
    elif identify == 'up':
        objs.append(up_trend)
    elif identify == 'down':
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

    if identify == 'both':
        up_trends = list()

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

        down_trends = list()

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
    elif identify == 'up':
        up_trends = results['Up Trend']

        up_labels = [letter for letter in string.ascii_uppercase[:len(up_trends)]]

        for up_trend, up_label in zip(up_trends, up_labels):
            for index, row in df[up_trend['from']:up_trend['to']].iterrows():
                df.loc[index, 'Up Trend'] = up_label

        return df
    elif identify == 'down':
        down_trends = results['Down Trend']

        down_labels = [letter for letter in string.ascii_uppercase[:len(down_trends)]]

        for down_trend, down_label in zip(down_trends, down_labels):
            for index, row in df[down_trend['from']:down_trend['to']].iterrows():
                df.loc[index, 'Down Trend'] = down_label

        return df
