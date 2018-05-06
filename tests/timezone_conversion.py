import unittest
from utils.dates import convert_datetime

class TestTimezoneConversion(unittest.TestCase):
    def setUp(self):
        self.utc = '2018-05-04T16:51:29.230Z'
        self.utc_morning = '2018-05-04T09:37:36.260Z'
        self.pyutc = '2018-05-04T16:51:29.230000+00:00'
        self.pst = '2018-05-04T09:51:29.230000-07:00'
        self.pst_formatted = '2018-05-04'
        self.est = '2018-05-04T12:51:29.230000-04:00'
        self.next_day = '2018-05-05'
        self.previous_day = '2018-05-04'

    def test_utc_to_pyutc(self):
        """Test the ISO format provided by the dataset and convert it to
        Python's representation.
        """

        new_date = convert_datetime(self.utc,
                                    target_tz='UTC')

        self.assertEqual(new_date, self.pyutc)

    def test_utc_to_pst(self):
        """Test UTC conversion to PST"""

        new_date = convert_datetime(self.utc,
                                    target_tz='America/Los_Angeles')

        self.assertEqual(new_date, self.pst)

    def test_target_format(self):
        """Test converstion of UTC to PST in the target format"""

        new_date = convert_datetime(self.utc,
                                    target_format='%Y-%m-%d',
                                    target_tz='America/Los_Angeles')

        self.assertEqual(new_date, self.pst_formatted)

    def test_utc_next_day(self):
        """Test conversion of UTC to a timezone in the next day"""

        new_date = convert_datetime(self.utc,
                                    target_format='%Y-%m-%d',
                                    target_tz='Asia/Macau')
        self.assertEqual(new_date, self.next_day)

    def test_utc_previous_day(self):
        """Test conversion of UTC to a timezone in the previous day"""

        new_date = convert_datetime(self.utc_morning,
                                    target_format='%Y-%m-%d',
                                    target_tz='America/Los_Angeles')

    def test_pst_to_utc(self):
        """Test PST conversion to UTC"""

        new_date = convert_datetime(self.pst,
                                    from_tz='America/Los_Angeles',
                                    target_tz='UTC')
        self.assertEqual(new_date, self.pyutc)

    def test_pst_to_est(self):
        """Test PST conversion to EST"""

        new_date = convert_datetime(self.pst,
                                    from_tz='America/Los_Angeles',
                                    target_tz='America/New_York')
        self.assertEqual(new_date, self.est)

    def test_same_offset_pst(self):
        """Test converting time to same timezone"""
        new_date = convert_datetime(self.pst,
                                    from_tz='America/Los_Angeles',
                                    target_tz='America/Vancouver')
        self.assertEqual(new_date, self.pst)

    def test_no_target_timezone(self):
        """Test converting to no target timezone"""
        new_date = convert_datetime(self.pyutc)
        self.assertEqual(new_date, self.pyutc)

        new_date = convert_datetime(self.pst)
        self.assertEqual(new_date, self.pst)
