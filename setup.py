#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import esplot


setup(
    name='beaker-es-plot',
    version='0.0.0',

    author='Andrew Grigorev',
    author_email='andrew@ei-grad.ru',

    description='ESPlot class for Beaker Notebook',
    long_description=esplot.__doc__,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers'
    ],

    install_requires=[
        'matplotlib',
        'dateutil',
    ],
)
