import itertools
import functools
import operator

def find_vampire_numbers(fangs):
	vampires = []
	for fang_combinations in itertools.combinations_with_replacement(range(10, 100), fangs):
		possible = functools.reduce(operator.mul, fang_combinations, 1)
		possible_chars = sorted(str(possible))
		fang_chars = sorted(''.join([str(fang) for fang in fang_combinations]))
		if possible_chars == fang_chars:
			print ">>>" + str(possible_chars)
			vampires.append((possible, ) + fang_combinations)
	return vampires

def main():
	fangs = 3
	solutions = find_vampire_numbers(fangs)
	print_style = '\n'.join([str(solution) for solution in solutions[1:]])
	print print_style

if __name__ == "__main__":
	main()