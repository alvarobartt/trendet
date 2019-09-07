#!/usr/bin/env python

from setuptools import setup, find_packages
import io


def readme():
    with io.open('README.md', encoding='utf-8') as f:
        return f.read()


setup(
    name='trendet',
    version='0.4',
    packages=find_packages(),
    url='https://github.com/alvarob96/trendet',
    download_url='https://github.com/alvarob96/trendet/archive/0.4.tar.gz',
    license='MIT License',
    author='Alvaro Bartolome',
    author_email='alvarob96@usal.es',
    description='trendet - is a Python package for trend detection on stock time series data',
    long_description=readme(),
    long_description_content_type='text/markdown',
    install_requires=[
        'investpy==0.8.8',
        'numpy>=1.17.0',
        'setuptools>=41.2.0'
    ],
    data_files=[],
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries",
    ],
    keywords='trend detection, stock analysis, stock, trend analysis',
    python_requires='>=3',
    project_urls={
        'Bug Reports': 'https://github.com/alvarob96/trendet/issues',
        'Source': 'https://github.com/alvarob96/trendet',
        'Documentation': 'https://trendet.readthedocs.io/'
    },
)
