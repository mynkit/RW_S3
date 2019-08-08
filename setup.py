# -*- coding: utf-8 -*-

from setuptools import find_packages, setup


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name="RW_S3",
    version="0.0.1",
    python_requires=">=3.5",
    packages=[
        "RW_S3",
    ],
    install_requires=_requires_from_file('requirements.txt'),
    url="https://github.com/mynkit/RW_S3",
)