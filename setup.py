# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    description = f.read()

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

requires = [
    ]

setup(
    name='chatworkpy',
    version='0.0.0',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/tys-hiroshi/chatworkpy',
    author='tys-hiroshi',
    author_email='tashiro.hiroshi@toyoko-sys.co.jp',
    license='MIT',
    keywords='chatwork module for python',
    packages=find_packages('chatworkpy'),  # Required
    package_dir = {'': 'chatworkpy'},
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python :: 3.8',
    ],
)
