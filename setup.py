# coding=utf-8
import os
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open('README.rst') as readme_file:
    long_description = readme_file.read()

setup(
    name='titanium',
    version='0.0.1',
    packages=['titanium'],
    include_package_data=True,
    license='MIT',
    description='Titanium is light-weight evaluator for PMML models based on NumPy.',
    long_description=long_description,
    url='https://github.com/vaclavcadek/keras2pmml',
    author='Václav Čadek',
    author_email='vaclavcadek@gmail.com',
    install_requires=['numpy==1.11.1'],
    tests_require=['scikit-learn==0.17.1', 'keras==1.0.6', 'theano==0.8.2', 'keras2pmml==0.1.0'],
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
