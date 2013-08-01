from unittest import TestCase
from anagramas import Anagramas

class AnagramasTest(TestCase):

	def testShouldAnagramThenA(self):
		anagrama = Anagramas('a')
		
		self.assertEqual(['a'], anagrama.generate())