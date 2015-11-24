def fib(n, incrementor):
    current = incrementor
    last = 0
    sequence = [0]
    while current <= n:
        sequence.append(current)
        temp = last
        last = current
        current = temp + last
    return sequence

def find_seq(x):
    if x == 0:
    	return 0
    init_sequence = fib(x, 1)
    for i in init_sequence[::-1]:
        if x % i == 0:
			return fib(x, int(x / i))


def main():
	print find_seq(0) #expected: [0]
	print find_seq(578) #expected: [0, 17, 17, 34, 51, 85, 136, 221, 357, 578]
	print find_seq(123456789) #expected: [0, 41152263, 41152263, 82304526, 123456789]

if __name__ == "__main__":
    main()