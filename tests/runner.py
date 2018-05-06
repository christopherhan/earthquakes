import unittest
import timezone_conversion, helpers

VERBOSITY=2

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(timezone_conversion))
suite.addTests(loader.loadTestsFromModule(helpers))

unittest.TextTestRunner(verbosity=VERBOSITY).run(suite)
