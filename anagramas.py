
def generate(word):
	result = set()

	if word == "":
		return [word]
	else:
		for w in generate(word[1:]):
			for pos in range(len(w)+1):
				result.add(w[:pos]+word[0]+w[pos:])
		
		return list(result)