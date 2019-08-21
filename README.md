# trendet - is a Python package for trend detection on stock time series data

[![Python Version](https://img.shields.io/pypi/pyversions/trendet.svg)](https://pypi.org/project/trendet/)
[![PyPi Version](https://img.shields.io/pypi/v/trendet.svg)](https://pypi.org/project/trendet/)
[![Package Status](https://img.shields.io/pypi/status/trendet.svg)](https://pypi.org/project/trendet/)
[![Build Status](https://dev.azure.com/alvarob96/alvarob96/_apis/build/status/alvarob96.trendet?branchName=master)](https://dev.azure.com/alvarob96/alvarob96/_build?definitionId=1&_a=summary)
[![Build Status](https://img.shields.io/travis/alvarob96/trendet/master.svg?label=Travis%20CI&logo=travis&logoColor=white)](https://travis-ci.org/alvarob96/trendet)
[![Documentation Status](https://readthedocs.org/projects/trendet/badge/?version=latest)](https://trendet.readthedocs.io/)
[![Downloads](https://img.shields.io/pypi/dm/trendet.svg?style=flat)](https://pypistats.org/packages/trendet)

<p align="center">
  <img src="https://raw.githubusercontent.com/alvarob96/trendet/master/docs/trendet.jpg"/>
</p>

## Introduction

**trendet** is a Python package to detect trends on the market so to analyze its behaviour. So on, this package
has been created to support [investpy](https://github.com/alvarob96/investpy) features when it comes to data retrieval
from different financial products such as stocks/equities, funds or ETFs. **trendet** is intended to be used combined
with **investpy**, but also with every OHLC `pandas.DataFrame`. 

## Installation

In order to get this package working you will need to install it using pip by typing on the terminal:

``$ python -m pip install trendet --upgrade``

Or just install the current release or a specific release version such as:

``$ python -m pip install trendet==0.1``

## Contribute

As this is an open source project it is open to contributions, bug reports, bug fixes, documentation improvements, 
enhancements and ideas.

Also there is an open tab of [issues](https://github.com/alvarob96/trendet/issues) where anyone can contribute opening 
new issues if needed or navigate through them in order to solve them or contribute to its solving.

## Disclaimer

This package has been created so to identify market trends based on stock historical data retrieved via 
[investpy](https://github.com/alvarob96/investpy) so to determine which trends have been prevailing on the market
based on a single stock/equity OHLC values.

Conclude that this is the result of a research project, so this package has been developed with research purposes and
no profit is intended.
