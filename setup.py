#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    try:
        from ez_setup import use_setuptools
        use_setuptools()
        from setuptools import setup
    except Exception, e:
        print "Forget setuptools, trying distutils..."
        from distutils.core import setup


description = "Tools for running, exploring, and analyzing models"

setup(
    name="Model Explorer",
    version="0.1.0",
    author="Terry Stewart",
    author_email="tcstewar@uwaterloo.ca",
    packages=['modex'],
    scripts=[],
    license="LICENSE",
    description=description,
    long_description=open('README.md').read(),
)
