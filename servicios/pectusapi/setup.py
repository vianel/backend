import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requires = [
    'flask',
    'sqlalchemy',
    'flask-sqlalchemy',
    'nose',
    'marshmallow',
    'flask-cors',
]


setup(
    name='t',
    version='0.1',
    description='Scan Social',
    classifiers=['Programming Language :: Python',],
    url='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    tests_require=requires
)
