import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import q3


class TestQ3(unittest.TestCase):

	def setUp(self):
		pass

	def test_troll_eat_her(self):
		tc = "It's fun to troll"
		try:
			q3.troll_check(tc)
		except q3.TheyreEatingHer:
			assert True
		else:
			assert False

	def test_troll_eat_me(self):
		tc = "If pointers wade through Nilbog"
		try:
			q3.troll_check(tc)
		except q3.ThenTheyreGoingToEatMe:
			assert True
		else:
			assert False

	def test_troll_replace(self):
		tc = "goblin 1 vs 0 hobgoblin"
		r = q3.troll_check(tc)
		self.assertEqual(r, "elf 1 vs 0 orc")

	def test_print_troll_check(self):
		found = q3.print_troll_checked("./test_q3.py")
		self.assertEqual(found, 1, "should have a troll")

	def test_split(self):
		self.assertEqual("this.is.not.the.ext".split(".")[-1], "ext", "incorrect ext")
