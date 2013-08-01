class Anagramas:

	def __init__(self, word):
		self.word = word
		self.result = [word]

	def generate(self):		
		if(len(self.word) > 1):
			self.result.append(self.word[::-1])

		return self.result


