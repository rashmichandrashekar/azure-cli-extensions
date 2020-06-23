#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from codecs import open
from setuptools import setup, find_packages

# TODO: Confirm this is the right version number you want and it matches your
# HISTORY.rst entry.
VERSION = '0.2.0'

# The full list of classifiers is available at
# https://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'License :: OSI Approved :: MIT License',
]

# TODO: Add any additional SDK dependencies here
DEPENDENCIES = []

with open('README.md', 'r', encoding='utf-8') as f:
    README = f.read()
with open('HISTORY.rst', 'r', encoding='utf-8') as f:
    HISTORY = f.read()

setup(
    name='healthcareapis',
    version=VERSION,
    description='Microsoft Azure Command-Line Tools HealthcareApisManagementClient Extension',
    # TODO: Update author and email, if applicable
    author='Microsoft Corporation',
    author_email='azpycli@microsoft.com',
    # TODO: consider pointing directly to your source code instead of the generic repo
    url='https://github.com/Azure/azure-cli-extensions',
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    install_requires=DEPENDENCIES,
    package_data={'azext_healthcareapis': ['azext_metadata.json']},
)
