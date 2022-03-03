FILE = sorted(map(int, open("input.txt").read().strip().split('\n')))
print(FILE)

D = []
for i in range(len(FILE)):
    for j in range(i + 100 + 1, len(FILE)):
        D.append((i + j) // 2)
print(len(D), max(D))  # 12002550 4948
