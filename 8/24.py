import re
print(max(map(len, re.findall("Z{2,}(.+?)Z{2,}", open(r".\24.txt").read()))))
