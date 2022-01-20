import re

FILE = open(".\\k8-52.txt").read()
values = list(map(lambda x: FILE[x.start():x.end()], re.finditer(r"(.)\1+", FILE)))
value = max(values, key=len)
print(value[0], len(value))  # 0 14
