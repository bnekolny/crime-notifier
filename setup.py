
from setuptools import setup, find_packages
import sys, os

setup(name='crime',
    version='',
    description="crime-notifier",
    long_description="crime-notifier",
    classifiers=[], 
    keywords='',
    author='Brett Nekolny',
    author_email='nekolny.brett@gmail.com',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    install_requires=[
        ### Required to build documentation
        # "Sphinx >= 1.0",
        ### Required for testing
        # "nose",
        # "coverage",
        ],
    setup_requires=[],
    entry_points="""
    """,
    namespace_packages=[],
    )
