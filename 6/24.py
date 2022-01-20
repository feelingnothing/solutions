import re
print(max(map(len, re.findall("Z+Y+X+", open(r".\24.txt").read()))))
