all_preferences = {}

# read a list of all_preferences from the .txt file
# this .txt file is a copy of the challenge input from Reddit
for line in open('preferences.txt').read().splitlines():
    person = line[0]
    prefs = line.split(', ')
    prefs.pop(0)
    all_preferences[person] = prefs

# not a particularly unique solution
# adapted https://en.wikipedia.org/wiki/Stable_marriage_problem#Algorithm
# O(n**2) time complexity
def stableMatching():
    free_husbands = [p for p in all_preferences if p==p.upper()]
    free_wives = [p for p in all_preferences if p==p.lower()]
    pairs = {}
    while free_husbands:
        man = free_husbands[0]
        woman = all_preferences[man].pop(0)
        if woman in free_wives:
            pairs[woman] = man
            free_wives.remove(woman)
            free_husbands.remove(man)
        else:
            rival = pairs[woman]
            if all_preferences[woman].index(man) < all_preferences[woman].index(rival):
                free_husbands.append(rival)
                free_husbands.remove(man)
                pairs[woman] = man
    return pairs

for wife,husband in stableMatching().items():
    print("({}: {})".format(husband,wife))
