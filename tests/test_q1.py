import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import q1


class TestQ1(unittest.TestCase):

	def setUp(self):
		pass

	def test_10_1_missing(self):
		test_values = range(1, 10)
		test_values = test_values[:5] + test_values[6:]
		assert(len(test_values) == 8)
		assert(q1.foo(test_values) == 6)

	def test_10_0_missing(self):
		test_values = range(1, 10)
		assert(q1.foo(test_values) == -1)

	def test_100_10_missing(self):
		test_values = range(1, 100)
		test_values = test_values[:50] + test_values[60:]
		assert(q1.foo(test_values) == 51)

	def test_10_1st_missing(self):
		test_values = range(2, 10)
		assert(q1.foo(test_values) == 1)

