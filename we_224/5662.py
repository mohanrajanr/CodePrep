from collections import *


def makedis(s, l):

    c = Counter(s + l)

    maxval = max(list(c.values()))
    maxelems = [key for key, value in c.items() if value == maxval]

    min_len = len(s) + len(l)
    for elem in maxelems:
        min_len = min(min_len, len([a for a in s+l if a != elem]))

    return min_len


def minChar(a, b):

    dist = makedis(a, b)

    maxord = max(a, b, key=lambda x: sum([ord(i) for i in x]))
    minord = b if maxord == a else a

    minord = sorted(minord)
    maxord = sorted(maxord)

    min_val = dist
    value = 0
    for elem in Counter(maxord).keys():
        value = minord.find(elem) + maxord.find(elem)
        min_val = min(min_val, value)

    return min_val


print(minChar("aba", "caa"))
print(minChar("dabadd", "cda"))
print(minChar("da", "cced"))
print(minChar("ace", "abe"))
