#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="mashuhelpa",
    version="1.15",
    description="Mashumaro without inheritance",
    long_description=open("README.md", encoding="utf8").read(),
    long_description_content_type="text/markdown",
    platforms="all",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 5 - Production/Stable",
    ],
    license="Apache License, Version 2.0",
    author="Dan Dees",
    url="https://github.com/dand-oss/mashuhelpa",
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=["dataclasses;python_version=='3.6'", "mashumaro",],
    include_package_data=True,
)
