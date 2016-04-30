from collections import Counter
from math import log2

def entropy(s):
  return -sum(i / len(s) * log2(i / len(s)) for i in Counter(s).values())

def isclose(f1, f2):
  allowed_error = 0.000000001
  return abs(f1 - f2) <= allowed_error

if __name__ == "__main__":
  test_cases = (
    ('122333444455555666666777777788888888', 2.794208683), 
    ('563881467447538846567288767728553786', 2.794208683),
    ('https://www.reddit.com/r/dailyprogrammer', 4.056198332),
    ('int main(int argc, char *argv[])', 3.866729296)
  )

  for case, solution in test_cases:
    computed_solution = entropy(case)
    print(str(computed_solution) + " ~= "  + str(solution) + " -> " + str(isclose(computed_solution, solution)))

