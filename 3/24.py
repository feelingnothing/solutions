S = open(r".\24.txt").read()
MAX = 0
K = 1

for i in range(1, len(S)):
    if (S[i], S[i - 1]) not in [("1", "2"), ("2", "1")]:
        K += 1
        continue
    if K > MAX:
        MAX = K
    K = 1

print(MAX)
