FILE = sorted(sum([list(map(float, i.split(","))) for i in open(".\\9.csv").read().strip().split("\n")], []))
FILTER = FILE[0], FILE[1], FILE[2], FILE[-3], FILE[-2], FILE[-1]
print(len(list(filter(lambda x: x not in FILTER, FILE))))
