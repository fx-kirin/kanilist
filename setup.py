import io
import os
import re

from setuptools import find_packages
from setuptools import setup
from pathlib import Path


def read(filename):
    file_path = Path(__file__).parent / filename
    text_type = type(u"")
    with open(file_path, mode="r", encoding="utf-8") as f:
        return re.sub(text_type(r":[a-z]+:`~?(.*?)`"), text_type(r"``\1``"), f.read())


def get_requires():
    r_path = Path(__file__).parent / "requirements.txt"
    if r_path.exists():
        with open(r_path) as f:
            required = f.read().splitlines()
    else:
        required = []

    return required


setup(
    name="kanilist",
    version="0.1.3",
    url="https://github.com/fx-kirin/kanilist",
    license='MIT',

    author="fx-kirin",
    author_email="fx.kirin@gmail.com",

    description="",
    long_description=read("README.rst"),

    packages=find_packages(exclude=('tests',)),

    install_requires=get_requires(),

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
