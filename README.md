# Python testing example

This is a simple solution to demonstrate some basic unit testing (with [unittest](https://docs.python.org/2/library/unittest.html)) with python including code coverage information (using [Coverage.py](coverage.readthedocs.io/)). This project is based on Python 2.7.

Dependencies can be restored using pip from requirements.txt.

Gather the code coverage information from the tests by executing the following:

```bash
coverage run -m unittest discover
coverage report
```

The provided `.coveragerc` file ignores the test files from coverage metrics and includes branch coverage information.