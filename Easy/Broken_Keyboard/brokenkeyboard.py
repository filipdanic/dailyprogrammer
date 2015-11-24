f = open("dict.txt")
letter_set = set(raw_input("Enter letters: ")); 
# It's trivial to check the word length and determine the longest word from here
# Here we just print all the word that fit the criteria thanks to issubset()
for word in f.read().split():
	if set(word).issubset(letter_set):
		print word