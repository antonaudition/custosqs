import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import json
import q2


class TestQ2(unittest.TestCase):
    def setUp(self):
        pass

    def test_format(self):
        tc = '{"timestamp":1496164686875,"bid":"34490.00","ask":"34495.00","last_trade":"34490.00","rolling_24_hour_volume":"572.307392","pair":"XBTZAR"}'
        dict = json.loads(tc)
        q2.pretty_print(dict)

    def test_poll(self):
        q2.poll(10, 60)
