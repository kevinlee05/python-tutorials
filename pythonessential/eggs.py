class Egg:
	def __init__ (self, kind = 'boiled'):
		self.kind = kind

	def whatKind(self):
		return self.kind

def main():
	boiled = Egg()
	scrambled = Egg('scrambled')
	print(boiled.whatKind(), scrambled.whatKind())

if __name__ == "__main__": main()