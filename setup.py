#! /usr/bin/env python2.5
# -*- coding: utf-8 -*-

__author__ = 'Travis Silvers, firestrand@gmail.com'

from setuptools import setup, find_packages


setup(
    name="PyBrain-GPU",
    version="0.0.1",
    description="PyBrain-GPU is a port of PyBrain the Swiss army knife for neural networking. GPU Optimized",
    license="BSD",
    keywords="Neural Networks Machine Learning GPGPU",
    url="http://pybrain.org",
    packages=find_packages(exclude=['examples', 'docs']),
    include_package_data=True,
    test_suite='pybraingpu.tests.runtests.make_test_suite',
    package_data={'pybraingpu': ['rl/environments/ode/models/*.xode']},
    install_requires=["numpy", "scipy", "theano"],
)