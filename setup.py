from setuptools import setup

setup(
    name='venmo2ynab',
    version='0.1',
    py_modules=['venmo2ynab'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        venmo2ynab=venmo2ynab:main
    ''',
)
