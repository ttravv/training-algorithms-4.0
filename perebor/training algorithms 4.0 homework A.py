from itertools import permutations

N = int(input())
numbers = list(range(1, N + 1))
perms = permutations(numbers)

for perm in perms:
    print(''.join(map(str, perm)))
