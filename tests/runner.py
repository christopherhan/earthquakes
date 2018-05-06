import unittest

import dates
import helpers
import events

VERBOSITY=2

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(dates))
suite.addTests(loader.loadTestsFromModule(helpers))
suite.addTests(loader.loadTestsFromModule(events))

unittest.TextTestRunner(verbosity=VERBOSITY).run(suite)
