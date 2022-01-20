import re
print(max(map(len, re.findall("Z(.+?)Z", open(r".\24.txt").read()))))
