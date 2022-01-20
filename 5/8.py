from itertools import product
print(len(list(filter(lambda x: x[0] > x[1] > x[2], product([0, 1, 2, 3, 4], repeat=3)))))
print(list(filter(lambda x: x[0] > x[1] > x[2], product([0, 1, 2, 3, 4], repeat=3))))
