import os
import sys
import warnings

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

path, script = os.path.split(sys.argv[0])
os.chdir(os.path.abspath(path))

install_requires = []

if sys.version_info < (2, 6):
    warnings.warn(
        'Python 2.5 is no longer officially supported by FerBuy. '
        'If you have any questions, please file an issue on Github or '
        'contact us at support@ferbuy.com.',
        DeprecationWarning)
    install_requires.append('requests >= 0.8.8, < 0.10.1')
    install_requires.append('ssl')
else:
    install_requires.append('requests >= 0.8.8')

# Don't import ferbuy module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'ferbuy'))
from version import VERSION

with open('LONG_DESCRIPTION.rst') as f:
    long_description = f.read()

# Get simplejson if we don't already have json
if sys.version_info < (3, 0):
    try:
        from util import json
    except ImportError:
        install_requires.append('simplejson')


setup(
    name='ferbuy',
    cmdclass={'build_py': build_py},
    version=VERSION,
    description='FerBuy Python bindings',
    long_description=long_description,
    author='FerBuy',
    author_email='support@ferbuy.com',
    url='https://ferbuy.com/',
    packages=['ferbuy', 'ferbuy.tests'],
    install_requires=install_requires,
    test_suite='ferbuy.tests.all',
    use_2to3=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ])
