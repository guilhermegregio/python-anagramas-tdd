class Anagramas:

	def __init__(self, word):
		self.word = word
		self.result = []

	def generate(self):

		if(len(self.word) == 1):
			self.result.append(self.word)

		if(len(self.word) == 2):
			self.result.append(self.word)
			self.result.append(self.word[::-1])

		if(len(self.word) == 3):
			for i in range(0, len(self.word)):
				for ii in range(0, len(self.word)):
					for iii in range(0, len(self.word)):
						if i != ii and ii != iii and i != iii:
							self.result.append(self.word[i] + self.word[ii] + self.word[iii])

		return self.result