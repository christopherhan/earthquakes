import unittest
import timezone_conversion

VERBOSITY=2

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(timezone_conversion))

unittest.TextTestRunner(verbosity=VERBOSITY).run(suite)
