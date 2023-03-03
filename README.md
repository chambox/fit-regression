# Python Library Template

This repository provides a generic Python library template  that users can fork and adapt to suit their needs. Note we call this repository `fit-regression`. You can always choose an appropriate name for you project. 

## Forking the Repository

To fork this repository:

Click the "Fork" button on the upper-right corner of this repository's main page. This will create a copy of this repository in your own GitHub account.

## Creating a Local Copy

To create a local copy of your forked repository:

1. Clone the repository to your local machine using the command git clone https://github.com/YOUR-USERNAME/fit-regression.git. Replace YOUR-USERNAME with your GitHub username.

2. Rename the directory name to suit your needs, in the example we use `fit-regression`.

3. Change into the repository directory using the command `cd fit-regression`.
4. Create a virtual environment, one way to do this is by first installing  `virtualenv` software.
  - For Python 3:

    * On macOS/Linux: python3 -m pip install --user virtualenv
    * On Windows: py -m pip install --user virtualenv

5. Create a virtual environment for the repository using the command `virtualenv venv`.

6. Activate the virtual environment using the command source `venv/bin/activate` (on macOS/Linux) or `venv\Scripts\activate` (on Windows).

7. Modify the `requirements.txt` file and add all your dependencies

8. Install the required dependencies using the command `pip install -r requirements.txt`.

9. Install your library too in editable mode by running the following command:

`pip install -e .
`

## Writing Tests

To write tests for each method or module you write:

Create a new Python file in the `tests` directory with the name `test_<module-name>.py` also see examples of tests in the `tests` directory. Replace `<module-name>` with the name of the module you want to test.

Import the module you want to test using the command from <module-name> import <function-name>.

Write test functions that call the functions you want to test and check their output using assertions. See the example in tests directory that we created for the `fit-regression` libary.

    
## Contributing

If you find any issues with this repository, or if you have any suggestions for improvements, please feel free to create a pull request or open an issue. We welcome contributions from the community.
