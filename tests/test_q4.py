import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import q4


class TestDB(unittest.TestCase):
    def setUp(self):
        pass

    def test_create(self):
        db = q4.SqLiteDriver("test.cache")
        db.insert("d62248ab691cbaba10ec14c16cf8f625", 18,
                  '$2b$18$4s_NMzD1A4H3rdPF9zrgQOisuPVLu3M2eJ_Sd4eBtQy8pWo3v3mci')
