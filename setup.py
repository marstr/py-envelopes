#!/usr/bin/env python

# Copyright 2019 Martin Strobel
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages
import re, io, os

VERSION = re.search(
    r'__version__\s*=\s*[rRfFuU]{0,2}[\'"]([^\'"]*)[\'"]',
    io.open(os.path.join('envelopes', '__init__.py'), encoding='utf_8_sig').read()
).group(1)

setup(
    name='lib-baronial',
    version=VERSION,
    author='Martin Strobel',
    author_email='martin.strobel@live.com',
    description='Tools for writing Python scripts to work with a baronial repository.',

    url='https://github.com/marstr/py-envelopes',
    packages=find_packages(
        exclude=('tests',),
    ),
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Office/Business :: Financial :: Accounting',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
    ],
)
