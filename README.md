# Summary 

1. Fork this repository 
2. Adapt

# Generic example
Fit a regression model

# Testing 
1. Install the library (using  `pip install -e .`) and dependencies in the `requirements.txt` in your virtual env. 
2. The `pip install -e .` installs the `fit-regression` library in editable mode (-e) and installs the dependencies listed in `setup.py`.
3. Run the tests: `python -m unittest discover tests`

This command runs all the tests in the tests directory using the unittest test runner.

# Building wheel 
To build a wheel package for your Python library, you can use the `bdist_wheel` command of `setuptools` package.

Here's an example of how to do this:

First, ensure that setuptools is installed in your Python environment. You can do this by running `pip install setuptools`.

Navigate to the root directory of your library where `setup.py` is located.

Run the following command to build the wheel package: `python setup.py bdist_wheel`

This command will build a wheel package in the dist directory.
You can now distribute the wheel package to others or install it on your own system using pip install <path_to_wheel>.

