from itertools import combinations, permutations

pess = ['ARTHUR', 'CLEBER', 'ALFRED', 'DUMMY']

for gp in permutations(pess, 3):
    print(gp)