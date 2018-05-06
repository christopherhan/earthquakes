import unittest
from utils.helpers import get_field_indices, lookup_field_values

class TestHelpers(unittest.TestCase):
    def setUp(self):

        self.data = [
            '2018-04-04T19:33:28.420Z', '33.3393333', '-117.143', '-0.44',
            '1.08', 'ml', '33', '61', '0.05644', '0.23', 'ci', 'ci37907567',
            '2018-04-04T20:50:09.922Z', '7km WSW of Pala, CA', 'earthquake',
            '0.37', '31.61','0.17', '24', 'reviewed', 'ci', 'ci'
        ]

        self.all_fields = [
            'time', 'latitude', 'longitude', 'depth', 'mag', 'magType', 'nst',
            'gap', 'dmin', 'rms', 'net', 'id', 'updated', 'place', 'type',
            'horizontalError', 'depthError', 'magError', 'magNst', 'status',
            'locationSource', 'magSource'
        ]
        self.select_fields = ['time', 'mag', 'type', 'locationSource']
        self.field_indices = {'time': 0, 'mag': 4, 'type': 14, 'locationSource': 20}
        self.field_values = {'time': '2018-04-04T19:33:28.420Z', 'mag': '1.08',
                             'type': 'earthquake', 'locationSource': 'ci' }
        self.filter_by = ('type', 'earthquake')

    def test_get_field_indices(self):
        indices = get_field_indices(self.select_fields, self.all_fields)
        self.assertEqual(indices, self.field_indices)
        self.assertNotEqual(self.field_indices['time'], 1)

    def test_lookup_field_values(self):
        values = lookup_field_values(self.field_indices, self.data,
                                     filter_by=self.filter_by)
        self.assertEqual(values['time'], '2018-04-04T19:33:28.420Z')
        self.assertEqual(values['locationSource'], 'ci')

    def test_lookup_field_values_nofilter(self):
        values = lookup_field_values(self.field_indices, self.data)
        self.assertEqual(values['time'], '2018-04-04T19:33:28.420Z')
        self.assertEqual(values['locationSource'], 'ci')
