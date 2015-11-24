import random
pieces = ["O", "I", "S", "Z", "L", "J", "T"]

def make_random_bag():
	string = ""
	for i in range(7):
		random.shuffle(pieces)
		string += "".join(pieces)
	string += pieces[random.randint(0,6)]
	return string

def main():
	print make_random_bag()

if __name__ == "__main__":
	main()