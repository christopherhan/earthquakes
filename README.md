# Earthquakes

Downloads and analyzes the 30-day M1.0 earthquake feed from USGS.gov.

## Getting Started

Clone the repo:

    $ git clone git@gitlab.com:christopherhan/earthquakes.git
    $ cd earthquakes

Ensure your PYTHONPATH contains the project:

    export PYTHONPATH=$PYTHONPATH:`pwd`

Install `requirements.txt` and ensure you are running Python >= 3.6:

    $ pip install -r requirements.txt
    $ which python
    /Users/chris/.virtualenvs/earthquakes/bin/python
    $ python --version
    Python 3.6.5

Execute `main.py` (ensure you're in the project root):

    $ python main.py


## Unit Tests

To run unit tests, run:

    $ python -m unittest tests/tests.py


You should see output similar to the following:

```
(earthquakes) Chriss-MacBook-Pro:earthquakes chris$ python tests/tests.py
.......
----------------------------------------------------------------------
Ran 7 tests in 0.003s

OK
```
