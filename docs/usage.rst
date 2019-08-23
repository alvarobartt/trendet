Usage
=====

As **trendet** is intended to be combined with **investpy**, the main functionality is to
detect trends on stock time series data so to analyse the market and which behaviour does it have
in certain date ranges.

In the example presented below, the ``identify_trends`` function will be used to detect 3 bearish/bullish trends
with a time window above 5 days, which implies that every bearish (decreasing) trend with a longer
duration than 5 days will be identified and so on added to a ``pandas.DataFrame`` which already contains
OHLC values, in new columns called `Up Trend` and `Down Trend` which will be labeled as specified, with letters from A
to Z by default.

.. code-block:: python

    import trendet

    import matplotlib.pyplot as plt
    import seaborn as sns

    sns.set(style='darkgrid')

    df = trendet.identify_trends(equity='bbva',
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

.. image:: https://raw.githubusercontent.com/alvarob96/trendet/master/docs/trendet_example.png
    :align: center

Additionally **trendet** allows the user to identify/detect all the up and down trends on the market
via the function `identify_all_trends` which has been included in 0.3 release. So on, the sample code for
its usage is as follows:

.. code-block:: python

    import trendet

    import matplotlib.pyplot as plt
    import seaborn as sns

    sns.set(style='darkgrid')

    df = identify_all_trends(equity='bbva',
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

.. image:: https://raw.githubusercontent.com/alvarob96/trendet/master/docs/trendet_example_all.png
    :align: center