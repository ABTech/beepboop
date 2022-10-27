#!/usr/bin/env python

import pathlib
from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()

long_description = (here/'README.md').read_text(encoding='utf-8')

setup(
    name="beepboop",
    description="Beep Boop Webserver",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    author="AB Tech",
    author_email="abtech@andrew.cmu.edu",
    python_requires='>=3.8, <4',
    packages=find_packages(),
    platforms=["any"],
    url="https://github.com/ABTech/beepboop",
    project_urls={
        'Bug Reports': 'https://github.com/ABTech/beepboop/issues',
        'Source': 'https://github.com/ABTech/beepboop',
    },
    classifiers=[
        'Framework :: Flask',
        'License :: OSI Approved :: MIT License',
        'Private :: Do Not Upload',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only'
    ],
    keywords='beep boop',
    entry_points = {
        'console_scripts': [
            'beepboop=beepboop.server:main'
        ],
    },
    install_requires=[
        'flask>=2,<3',
        'requests>=2,<3'
    ],
    extras_require={
        'deploy': [
            'gunicorn>=20,<21'
        ]
    }
)
