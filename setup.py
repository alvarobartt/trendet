# Copyright 2019-2020 Alvaro Bartolome
# See LICENSE for details.

from setuptools import setup, find_packages
import io


def readme():
    with io.open('README.md', encoding='utf-8') as f:
        return f.read()

def requirements():
    reqs = list()
    with io.open('requirements.txt', encoding='utf-8') as f:
        for line in f.readlines():
            reqs.append(line.strip())
    return reqs


setup(
    name='trendet',
    version='0.6',
    packages=find_packages(),
    url='https://github.com/alvarobartt/trendet',
    download_url='https://github.com/alvarobartt/trendet/archive/0.6.tar.gz',
    license='MIT License',
    author='Alvaro Bartolome',
    author_email='alvarob96@usal.es',
    description='trendet - Trend detection on stock time series data',
    long_description=readme(),
    long_description_content_type='text/markdown',
    install_requires=requirements(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries",
    ],
    keywords='trend detection, stock analysis, stock, trend analysis',
    python_requires='>=3',
    project_urls={
        'Bug Reports': 'https://github.com/alvarobartt/trendet/issues',
        'Source': 'https://github.com/alvarobartt/trendet',
        'Documentation': 'https://trendet.readthedocs.io/'
    },
)
