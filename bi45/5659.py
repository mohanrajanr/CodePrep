import collections


def minimumLength(s: str) -> int:
    qu = collections.deque(s)
    prefix = 0
    suffix = len(s) - 1

    while qu and qu[prefix] == qu[suffix] and prefix != suffix:

        while prefix + 1 < suffix and qu[prefix] == qu[prefix + 1]:
            suffix -= 1
            qu.popleft()

        while suffix - 1 > prefix and qu[suffix] == qu[suffix - 1]:
            suffix -= 1
            qu.pop()

        qu.popleft()
        qu.pop()
        suffix -= 2

    return len(qu)


print(minimumLength("ca"))
print(minimumLength("cabaabac"))
print(minimumLength("aabccabba"))
