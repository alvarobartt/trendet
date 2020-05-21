# trendet - Trend detection on stock time series data

[![Python Version](https://img.shields.io/pypi/pyversions/trendet.svg)](https://pypi.org/project/trendet/)
[![PyPi Version](https://img.shields.io/pypi/v/trendet.svg)](https://pypi.org/project/trendet/)
[![Package Status](https://img.shields.io/pypi/status/trendet.svg)](https://pypi.org/project/trendet/)
[![Build Status](https://dev.azure.com/alvarobartt/alvarobartt/_apis/build/status/alvarobartt.trendet?branchName=master)](https://dev.azure.com/alvarobartt/alvarobartt/_build?definitionId=1&_a=summary)
[![Build Status](https://img.shields.io/travis/alvarobartt/trendet/master.svg?label=Travis%20CI&logo=travis&logoColor=white)](https://travis-ci.org/alvarobartt/trendet)
[![Documentation Status](https://readthedocs.org/projects/trendet/badge/?version=latest)](https://trendet.readthedocs.io/)
[![codecov](https://codecov.io/gh/alvarobartt/trendet/branch/master/graph/badge.svg)](https://codecov.io/gh/alvarobartt/trendet)
[![Downloads](https://img.shields.io/pypi/dm/trendet.svg?style=flat)](https://pypistats.org/packages/trendet)

<p align="center">
  <img src="https://raw.githubusercontent.com/alvarobartt/trendet/master/docs/_static/trendet.jpg"/>
</p>

## Introduction

**trendet** is a Python package to detect trends on the market so to analyze its behaviour. So on, this package
has been created to support [investpy](https://github.com/alvarobartt/investpy) features when it comes to data retrieval
from different financial products such as stocks, funds or ETFs; and it is intended to be combined with it, 
but also with every `pandas.DataFrame`, formatted as OHLC.

Anyways, **trendet** can also be used to identify trends from any `pandas.DataFrame` which contains any column with
`int64` or `float64` values, even though it is intended to be used with stock data; it can also be used for any
`pandas.DataFrame`.

## Installation

In order to get this package working you will need to install it using pip by typing on the terminal:

``$ python -m pip install trendet --upgrade``

Or just install the current release or a specific release version such as:

``$ python -m pip install trendet==0.7``

## Usage

As **trendet** is intended to be combined with **investpy**, the main functionality is to
detect trends on stock time series data so to analyse the market and which behaviour does it have
in certain date ranges.

In the example presented below, the ``identify_all_trends`` function will be used to detect every bearish/bullish trend
with a time window above 5 days, which, for example, implies that every bearish (decreasing) trend with a longer
length than 5 days will be identified as a down trend and so on added to a ``pandas.DataFrame`` which already contains
OHLC values, in new columns called **Up Trend** and **Down Trend** which will be labeled as specified, with letters 
from A to Z by default.

````python
import trendet

import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='darkgrid')

df = trendet.identify_all_trends(stock='BBVA',
                                 country='Spain',
                                 from_date='01/01/2018',
                                 to_date='01/01/2019',
                                 window_size=5,
                                 identify='both')

df.reset_index(inplace=True)

plt.figure(figsize=(20, 10))

ax = sns.lineplot(x=df.index, y=df['Close'])
ax.set(xlabel='Date')

labels = df['Up Trend'].dropna().unique().tolist()

for label in labels:
    sns.lineplot(x=df[df['Up Trend'] == label].index,
                 y=df[df['Up Trend'] == label]['Close'],
                 color='green')

    ax.axvspan(df[df['Up Trend'] == label].index[0],
               df[df['Up Trend'] == label].index[-1],
               alpha=0.2,
               color='green')

labels = df['Down Trend'].dropna().unique().tolist()

for label in labels:
    sns.lineplot(x=df[df['Down Trend'] == label].index,
                 y=df[df['Down Trend'] == label]['Close'],
                 color='red')

    ax.axvspan(df[df['Down Trend'] == label].index[0],
               df[df['Down Trend'] == label].index[-1],
               alpha=0.2,
               color='red')
               
locs, _ = plt.xticks()
labels = []

for position in locs[1:-1]:
    labels.append(str(df['Date'].loc[position])[:-9])

plt.xticks(locs[1:-1], labels)
plt.show()
````

Further usage insights can be found on the [docs](https://trendet.readthedocs.io/) or on the following 
[gist](https://gist.github.com/alvarobartt/98f94dcfec59f78a16ad2edbf464ce75#file-identify_all_trends-py). Anyways, 
feel free to create your own scripts on how you use **trendet** or how can it be used in order to improve its features.

## Contribute

As this is an open source project it is open to contributions, bug reports, bug fixes, documentation improvements, 
enhancements and ideas.

Also there is an open tab of [issues](https://github.com/alvarobartt/trendet/issues) where anyone can contribute opening 
new issues if needed or navigate through them in order to solve them or contribute to its solving.

## Disclaimer

This package has been created so to identify market trends based on stock historical data retrieved via 
[investpy](https://github.com/alvarobartt/investpy) so to determine which trends have been prevailing on the market
based on a single stock OHLC values.

Conclude that this is the result of a research project, so this package has been developed with research purposes and
no profit is intended.

Plots have been generated with both [matplotlib](https://pypi.org/project/matplotlib/) and 
[seaborn](https://pypi.org/project/seaborn/).
