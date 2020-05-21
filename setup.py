# Copyright 2019-2020 Alvaro Bartolome
# See LICENSE for details.

from setuptools import setup, find_packages
import io


def readme():
    with io.open('README.md', encoding='utf-8') as f:
        return f.read()

def requirements(filename):
    reqs = list()
    with io.open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            reqs.append(line.strip())
    return reqs


setup(
    name='trendet',
    version='0.7',
    packages=find_packages(),
    url='https://github.com/alvarobartt/trendet',
    download_url='https://github.com/alvarobartt/trendet/archive/0.7.tar.gz',
    license='MIT License',
    author='Alvaro Bartolome',
    author_email='alvarob96@usal.es',
    description='Trend detection on stock time series data',
    long_description=readme(),
    long_description_content_type='text/markdown',
    install_requires=requirements(filename="requirements.txt"),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
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
    keywords=', '.join([
        "trend detection", "stock analysis", "stock", "trend analysis",
        "stock trends", "financial trends"
    ]),
    python_requires='>=3',
    extras_require={
        "tests": requirements(filename='tests/requirements.txt'),
        "docs": requirements(filename='docs/requirements.txt')
    },
    project_urls={
        'Bug Reports': 'https://github.com/alvarobartt/trendet/issues',
        'Source': 'https://github.com/alvarobartt/trendet',
        'Documentation': 'https://trendet.readthedocs.io/'
    },
)
