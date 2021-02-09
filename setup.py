#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='django-scheduler-otm',
    version='0.0.1',
    description='A calendaring app for OpenTreeMap.',
    author='Chris Ward',
    author_email='chris.dev.ward@gmail.com',
    url='https://github.com/cwardcode/django-scheduler-otm',
    packages=[
        'schedule',
        'schedule.feeds',
        'schedule.models',
        'schedule.migrations',
        'schedule.templatetags',
    ],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ],
    python_requires=">=2.7",
    install_requires=[
        'Django>=1.11',
        'python-dateutil>=2.1',
        'pytz>=2013.9',
        'icalendar>=3.8.4',
    ],
    license='BSD',
    test_suite='runtests.runtests',
)
