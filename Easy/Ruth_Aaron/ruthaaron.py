def factor_sum(n):
	total_sum = 0
	for i in range(2,n+1):
		if n%i == 0:
			total_sum += i
			while n%i == 0:
				n /=i
		i+=1
	return total_sum

def main():

	for x in range(2,2000): # all Ruth-Aaron pairs from [2,3] to [1999,2000]
		if factor_sum(x) == factor_sum(x+1):
			print "("+str(x)+", "+str(x+1)+") VALID"

if __name__ == "__main__":
	main()