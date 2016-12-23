#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'requests>=2.0.0',
    'beautifulsoup4>=4.5.0',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pyperi',
    version='0.2.0',
    description="Use Periscope with Python.",
    long_description=readme + '\n\n' + history,
    author="Tom Smith",
    author_email='tom@takeontom.com',
    url='https://github.com/takeontom/pyperi',
    packages=[
        'pyperi',
    ],
    package_dir={'pyperi':
                 'pyperi'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='pyperi',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
