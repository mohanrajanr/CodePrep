import collections


def nice(s):

    maxs = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            # print(s[i:j+1])
            elem = s[i:j+1]
            c = collections.Counter(elem)

            all_True = True
            for k in elem:
                # print(k, k.upper() in c and k.lower() in c)
                if not k.upper() in c or not k.lower() in c:
                    all_True = False

            if all_True:
                maxs = max(maxs, elem, key=len)

    return maxs

print(nice("YazaAay"))
print(nice("Bb"))
print(nice("c"))
print(nice("dDzeE"))
print(nice("jcJ"))
