Usage
=====

As **trendet** is intended to be combined with **investpy**, the main functionality is to detect trends on stock time
series data so to analyse the market and which behaviour does it have in certain date ranges. Anyways, **trendet** can
also be used with any custom ``pandas.DataFrame``.

Identify Custom Trends of investpy DataFrames
---------------------------------------------

In the example presented below, the ``identify_trends`` function will be used to detect 3 bearish/bullish trends
with a time window above 5 days, which implies that every bearish (decreasing) trend with a longer
duration than 5 days will be identified and so on added to a ``pandas.DataFrame`` which already contains
OHLC values, in new columns called ``Up Trend`` and ``Down Trend`` which will be labeled as specified, with letters from A
to Z by default.

.. code-block:: python

    import trendet

    import matplotlib.pyplot as plt
    import seaborn as sns

    sns.set(style='darkgrid')

    df = trendet.identify_trends(stock='BBVA',
                                 country='Spain',
                                 from_date='01/01/2018',
                                 to_date='01/01/2019',
                                 window_size=5,
                                 trend_limit=3,
                                 labels=['A', 'B', 'C'])

    df.reset_index(inplace=True)

    with plt.style.context('paper'):
        plt.figure(figsize=(20, 10))

        ax = sns.lineplot(x=df['Date'], y=df['Close'])

        values = list()

        value = {
            'trend': 'Up Trend',
            'color': 'green',
        }

        values.append(value)

        value = {
            'trend': 'Down Trend',
            'color': 'red',
        }

        values.append(value)

        for label in ['A', 'B', 'C']:
            for value in values:
                sns.lineplot(x=df[df[value['trend']] == label]['Date'], y=df[df[value['trend']] == label]['Close'], color=value['color'])
                ax.axvspan(df[df[value['trend']] == label]['Date'].iloc[0], df[df[value['trend']] == label]['Date'].iloc[-1], alpha=0.2, color=value['color'])

        plt.show()

So on, the resulting plot which will be outputted from the previous block of code will look like:

.. image:: https://raw.githubusercontent.com/alvarobartt/trendet/master/docs/_static/trendet_example.png
    :align: center

Identify All Trends of investpy DataFrame
-----------------------------------------

Additionally **trendet** allows the user to identify/detect all the up and down trends on the market
via the function ``identify_all_trends`` which has been included in 0.6 release. So on, the sample code for
its usage is as follows:

.. code-block:: python

    import trendet

    import matplotlib.pyplot as plt
    import seaborn as sns

    sns.set(style='darkgrid')

    df = trendet.identify_all_trends(stock='BBVA',
                                     country='Spain',
                                     from_date='01/01/2018',
                                     to_date='01/01/2019',
                                     window_size=5)

    df.reset_index(inplace=True)

    with plt.style.context('paper'):
        plt.figure(figsize=(20, 10))

        ax = sns.lineplot(x=df['Date'], y=df['Close'])

        labels = df['Up Trend'].dropna().unique().tolist()

        for label in labels:
            sns.lineplot(x=df[df['Up Trend'] == label]['Date'],
                         y=df[df['Up Trend'] == label]['Close'],
                         color='green')

            ax.axvspan(df[df['Up Trend'] == label]['Date'].iloc[0],
                       df[df['Up Trend'] == label]['Date'].iloc[-1],
                       alpha=0.2,
                       color='green')

        labels = df['Down Trend'].dropna().unique().tolist()

        for label in labels:
            sns.lineplot(x=df[df['Down Trend'] == label]['Date'],
                         y=df[df['Down Trend'] == label]['Close'],
                         color='red')

            ax.axvspan(df[df['Down Trend'] == label]['Date'].iloc[0],
                       df[df['Down Trend'] == label]['Date'].iloc[-1],
                       alpha=0.2,
                       color='red')

        plt.show()

Which as described before, plots all the trends identified on the specified stock time series
data removing overlapped trends keeping just the longer trend as minor trends are ignored. So the
output of the previous block of code on **trendet** usage is the following plot:

.. image:: https://raw.githubusercontent.com/alvarobartt/trendet/master/docs/_static/trendet_example_all.png
    :align: center

Identify Trends of Custom DataFrame
-----------------------------------

Anyways, you can also use **trendet** for custom any ``pandas.DataFrame`` even though it is intended to be used combined
with **investpy**. So on, via using ``identify_df_trends()`` function the trends from the specified ``pandas.DataFrame`` can be
identified, just specifying the column from where the trends wants to be identified. In the example proposed below, an
**investpy** ``pandas.DataFrame`` is being used, but you can use any other ``pandas.DataFrame`` which matches the specified conditions
which are that the values can just be ``int64`` or ``float64`` and the specified column should be in the ``pandas.DataFrame``.

.. code-block:: python

    import trendet
    import investpy

    import matplotlib.pyplot as plt
    import seaborn as sns

    sns.set(style='darkgrid')

    test = investpy.get_stock_historical_data(stock='REP',
                                              country='Spain',
                                              from_date='01/01/2018',
                                              to_date='01/01/2019')

    res = trendet.identify_df_trends(df=test, column='Close')

    res.reset_index(inplace=True)

    with plt.style.context('paper'):
        plt.figure(figsize=(20, 10))

        ax = sns.lineplot(x=res['Date'], y=res['Close'])

        labels = res['Up Trend'].dropna().unique().tolist()

        for label in labels:
            sns.lineplot(x=res[res['Up Trend'] == label]['Date'],
                         y=res[res['Up Trend'] == label]['Close'],
                         color='green')

            ax.axvspan(res[res['Up Trend'] == label]['Date'].iloc[0],
                       res[res['Up Trend'] == label]['Date'].iloc[-1],
                       alpha=0.2,
                       color='green')

        labels = res['Down Trend'].dropna().unique().tolist()

        for label in labels:
            sns.lineplot(x=res[res['Down Trend'] == label]['Date'],
                         y=res[res['Down Trend'] == label]['Close'],
                         color='red')

            ax.axvspan(res[res['Down Trend'] == label]['Date'].iloc[0],
                       res[res['Down Trend'] == label]['Date'].iloc[-1],
                       alpha=0.2,
                       color='red')

        plt.show()

Which outputs the following plot:

.. image:: https://raw.githubusercontent.com/alvarobartt/trendet/master/docs/_static/trendet_example_df.png
    :align: center