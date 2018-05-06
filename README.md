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

To run unit tests, execute the test runner:

    $ python tests/runner.py


You should see output similar to the following:

```
$ python tests/runner.py
test_pst_to_est (timezone_conversion.TestTimezoneConversion)
Test PST conversion to EST ... ok
test_pst_to_utc (timezone_conversion.TestTimezoneConversion)
Test PST conversion to UTC ... ok
test_target_format (timezone_conversion.TestTimezoneConversion)
Test converstion of UTC to PST in the target format ... ok
test_utc_next_day (timezone_conversion.TestTimezoneConversion)
Test conversion of UTC to a timezone in the next day ... ok
test_utc_previous_day (timezone_conversion.TestTimezoneConversion)
Test conversion of UTC to a timezone in the previous day ... ok
test_utc_to_pst (timezone_conversion.TestTimezoneConversion)
Test UTC conversion to PST ... ok
test_utc_to_pyutc (timezone_conversion.TestTimezoneConversion)
Test the ISO format provided by the dataset and convert it to ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.003s

OK
```
