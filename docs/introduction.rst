Introduction
============

**trendet** is a Python package to detect trends on the market so to analyze its behaviour. So on, this package
has been created to support `investpy <https://github.com/alvarob96/investpy>`_ features when it comes to data retrieval
from different financial products such as stocks/equities, funds or ETFs; and it is intended to be combined with it,
but also with every ``pandas.DataFrame``, formatted as OHLC.

Anyways, **trendet** can also be used to identify trends from any `pandas.DataFrame` which contains any column with
`int64` or `float64` values, even though it is intended to be used with stock data; it can also be used for any
`pandas.DataFrame`.