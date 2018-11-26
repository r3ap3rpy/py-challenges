"""
Isogram is a word that has no repeating letters, consecutive or non-consecutive.
Empty String is also an isogram.
"""
from functools import reduce
import unittest

TestWords = ["isogram","aba","MoOse","Dermatoglyphics","isIsogram",""]

def is_isogram(word):
	if len(word) == 0:
		return True
	return True if reduce(lambda x, y: x*y, [word.lower().count(_) for _ in word.lower()]) == 1 else False

class IsoGramTester(unittest.TestCase):
	def setUp(self):
		self.is_isogram = is_isogram

	def test_isogram(self):
		self.assertEqual(self.is_isogram("isogram"),True)

	def test_aba(self):
		self.assertEqual(self.is_isogram("aba"),False)

	def test_MoOse(self):
		self.assertEqual(self.is_isogram("MoOse"),False)

	def test_Dermatoglyphics(self):
		self.assertEqual(self.is_isogram("Dermatoglyphics"),True)

	def test_isIsogram(self):
		self.assertEqual(self.is_isogram("isIsogram"),False)

	def test_is_empty(self):
		self.assertEqual(self.is_isogram(""),True)


if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(IsoGramTester)
	unittest.TextTestRunner(verbosity = 2).run(suite)



	

