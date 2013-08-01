from unittest import TestCase
from anagramas import Anagramas

class AnagramasTest(TestCase):

	def testShouldAnagramThenA(self):
		anagrama = Anagramas('a')
		
		self.assertEqual(['a'], anagrama.generate())

	def testShouldAnagramThenWordTwoLetters(self):
		anagrama = Anagramas('ab')
		
		self.assertEqual(['ab', 'ba'], anagrama.generate())

	def testShouldAnagramThenWordTwoLettersInverse(self):
		anagrama = Anagramas('ba')
		
		self.assertEqual(['ba', 'ab'], anagrama.generate())

	def testShouldAnagramThenWordThreeLetters(self):
		anagrama = Anagramas('abc')

		self.assertEqual(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'], anagrama.generate())