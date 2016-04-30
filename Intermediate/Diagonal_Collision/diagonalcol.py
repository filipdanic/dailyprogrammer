from fractions import gcd

def crossed_squares(x, y):
  return x + y - gcd(x, y)

if __name__ == "__main__":
  test_cases = ((3, 9, 9), (21, 2, 22), (168, 189, 336), (100, 101, 200))
  for x, y, solution in test_cases:
    computed_solution = crossed_squares(x, y)
    print(str(computed_solution) + ' == ' + str(solution) + ' -> ' + str(computed_solution == solution))

