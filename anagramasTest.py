from unittest import TestCase
import anagramas

class AnagramasTest(TestCase):

	def test_should_return_anagram_word_with_a_letter(self):
		self.assertEqual(['a'], anagramas.generate('a'))

	def test_should_return_anagram_word_with_repeated_letters(self):
		self.assertEqual(['aa'], anagramas.generate('aa'))

	def test_should_return_anagram_ab_result_ab_ba(self):
		self.assertEqual('ab ba'.split(' '), anagramas.generate('ab'))

	def test_should_return_anagram_of_the_word_bori(self):
		anagramaBiro = ['irbo', 'iorb', 'brio', 'bori', 'orib', 'oibr', 'obir', 'boir', 'bior', 'orbi', 'biro', 'rboi', 'ibro', 'robi', 'riob', 'ibor', 'roib', 'obri', 'iobr', 'rbio', 'ribo', 'broi', 'irob', 'oirb']
		self.assertEqual(anagramaBiro, anagramas.generate('bori'))
