from setuptools import setup, find_packages

setup(
    name='fit-regression',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
    ],
)   