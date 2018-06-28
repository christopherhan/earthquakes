# Earthquakes

Downloads and analyzes the 30-day M1.0 earthquake feed from USGS.gov.
## Contents
1. [Getting Started](#getting-started)
2. [Implementations](#implementations)
3. [Results](#results)
4. [Unit Tests](#unit-tests)
5. [Troubleshooting](#troubleshooting)


## [Getting Started](#getting-started)
Ensure you're running Python >= 3.6. Python's f-strings are utilized are only available in versions >= 3.6:

    $ which python
    /Users/chris/.virtualenvs/earthquakes/bin/python
    $ python --version
    Python 3.6.5

Clone the repo and ensure the project is added to your PYTHONPATH:

    $ git clone git@github.com:christopherhan/earthquakes.git
    $ cd earthquakes
    $ export PYTHONPATH=$PYTHONPATH:`pwd`

Install packages in `requirements.txt`:

    $ pip install -r requirements.txt


Execute `main.py` or `main2.py`:

    $ pwd
    /path/to/earthquakes
    $ python main.py # Invoke implementation 1
    $ python main2.py # Invoke implementation 2


## [Implementations](#implementations)

There are two implementations available:

1. `main.py`
2. `main2.py`

The first implementation was the first pass at the challenge and is mostly
procedural.

The second implementation is a more general, object-oriented approach
and is inspired by Django's object managers with custom manager methods.


## [Results](#results)

```
$ python main2.py
############ Question 1 Results ############
"ak"


############ Question 2 Results ############
{"2018-04-04": 35, "2018-04-05": 222, "2018-04-06": 223, "2018-04-07": 247, "2018-04-08": 270, "2018-04-09": 194, "2018-04-10": 183, "2018-04-11": 299, "2018-04-12": 282, "2018-04-13": 169, "2018-04-14": 222, "2018-04-15": 185, "2018-04-16": 199, "2018-04-17": 216, "2018-04-18": 184, "2018-04-19": 212, "2018-04-20": 211, "2018-04-21": 198, "2018-04-22": 219, "2018-04-23": 239, "2018-04-24": 192, "2018-04-25": 219, "2018-04-26": 200, "2018-04-27": 171, "2018-04-28": 226, "2018-04-29": 218, "2018-04-30": 206, "2018-05-01": 262, "2018-05-02": 282, "2018-05-03": 239, "2018-05-04": 155}


############ Question 2 Extra Credit (America/Los_Angeles) ############
{"2018-04-04": 100, "2018-04-05": 222, "2018-04-06": 224, "2018-04-07": 262, "2018-04-08": 252, "2018-04-09": 179, "2018-04-10": 218, "2018-04-11": 338, "2018-04-12": 200, "2018-04-13": 184, "2018-04-14": 228, "2018-04-15": 179, "2018-04-16": 194, "2018-04-17": 218, "2018-04-18": 184, "2018-04-19": 207, "2018-04-20": 223, "2018-04-21": 202, "2018-04-22": 233, "2018-04-23": 239, "2018-04-24": 171, "2018-04-25": 223, "2018-04-26": 188, "2018-04-27": 193, "2018-04-28": 210, "2018-04-29": 228, "2018-04-30": 223, "2018-05-01": 271, "2018-05-02": 259, "2018-05-03": 222, "2018-05-04": 105}


############ Question 3 Results ############
{"ci": "1.51", "hv": "2.02", "nc": "1.48", "uw": "1.52", "ak": "1.74", "uu": "1.55", "us": "4.06", "mb": "1.52", "ld": "1.33", "pr": "2.63", "nn": "1.36", "nm": "1.85", "tul": "2.76", "se": "2.40", "ismp": "2.04", "ott": "2.73"}


############ Question 4 Results ############
{"ci": "1.51"}


############ Question 4 extra credit (Querying "ak") ############
# See implementation in earthquakes.py. Note that sum is not being stored.
{"average": "1.74", "count": 2317}

```


## [Unit Tests](#unit-tests)

To run unit tests, execute the test runner:

```
$ python tests/runner.py
test_no_target_timezone (dates.TestTimezoneConversion)
Test converting to no target timezone ... ok
test_pst_to_est (dates.TestTimezoneConversion)
Test PST conversion to EST ... ok
test_pst_to_utc (dates.TestTimezoneConversion)
Test PST conversion to UTC ... ok
test_same_offset_pst (dates.TestTimezoneConversion)
Test converting time to same timezone ... ok
test_target_format (dates.TestTimezoneConversion)
Test converstion of UTC to PST in the target format ... ok
test_utc_next_day (dates.TestTimezoneConversion)
Test conversion of UTC to a timezone in the next day ... ok
test_utc_previous_day (dates.TestTimezoneConversion)
Test conversion of UTC to a timezone in the previous day ... ok
test_utc_to_pst (dates.TestTimezoneConversion)
Test UTC conversion to PST ... ok
test_utc_to_pyutc (dates.TestTimezoneConversion) ... ok
test_get_column_indices (helpers.TestHelpers) ... ok
test_lookup_column_values (helpers.TestHelpers) ... ok
test_lookup_column_values_nofilter (helpers.TestHelpers) ... ok
test_average_magnitude_location (events.TestEventManager)
Test getting the average magnigude for a location ... ok
test_average_magnitude_locations (events.TestEventManager)
Test getting the average magnitude for a single location ... ok
test_daily_histogram (events.TestEventManager)
Test generating daily histogram ... ok
test_max_earthquakes_location (events.TestEventManager)
Test getting location with highest earthquakes ... ok

----------------------------------------------------------------------
Ran 16 tests in 0.010s

OK
```

## [Troubleshooting](#troubleshooting)

#### `ModuleNotFoundError` while running a script

```
$ python tests/runner.py
Traceback (most recent call last):
  File "tests/runner.py", line 3, in <module>
    import dates
  File "/Users/chris/Projects/earthquakes/tests/dates.py", line 2, in <module>
    from utils.dates import convert_datetime
ModuleNotFoundError: No module named 'utils'
```

Ensure the project is included in `$PYTHONPATH` by running the following command:

```
$ cd /path/to/project_root
$ export PYTHONPATH=$PYTHONPATH:`pwd`
```
