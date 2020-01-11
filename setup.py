#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name="scalene-repro",
    version="0.1.0",
    url="https://github.com/jessemyers/scalene-repro",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=[
        "scalene>=0.5.6",
    ],
    entry_points={
        "console_scripts": [
            "example = example:main",
        ],
    },
)
