s = input().strip()
q = int(input().strip())
requests = [[int(x) for x in input().split()] for _ in range(q)]

X = 257
P = 10 ** 9 + 7

def is_equal(pos1: int, pos2: int, lenght, zeroes, ones):
    return (
            (zeroes[pos1 + lenght - 1] + zeroes[pos2 - 1] * ones[lenght]) % P ==
            (zeroes[pos2 + lenght - 1] + zeroes[pos1 - 1] * ones[lenght]) % P
    )

original_len = len(s)
s = ' ' + s
zeroes = [0] * (original_len + 1)
ones = [1] * (original_len + 1)
for i in range(1, original_len + 1):
    zeroes[i] = (zeroes[i - 1] * X + ord(s[i])) % P
    ones[i] = (ones[i - 1] * X) % P

for lenght, pos1, pos2 in requests:
    print('yes' if is_equal(pos1 + 1, pos2 + 1, lenght, zeroes, ones) else 'no')