def largestMerge(word1: str, word2: str) -> str:
    merge = []
    common = []
    w1 = list(word1[::-1])
    w2 = list(word2[::-1])

    while len(w1) and len(w2):
        # print(w1[-1], w2[-1], common, merge)
        if w1[-1] > w2[-1]:
            if common:
                merge.extend(common)
                w2.extend(common[::-1])
                common = []
            merge.append(w1[-1])
            w1.pop()
        elif w2[-1] > w1[-1]:
            if common:
                merge.extend(common)
                w1.extend(common[::-1])
                common = []
            merge.append(w2[-1])
            w2.pop()
        else:
            common.append(w1[-1])
            w1.pop()
            w2.pop()

    if common:
        merge.extend(common)
        merge.extend(common)

    if len(w1):
        merge.extend(w1[::-1])

    if len(w2):
        merge.extend(w2[::-1])

    print(common, w1, w2)

    return "".join(merge)

print(largestMerge("cabaa", "bcaaa"), "cbcabaaaaa")
print(largestMerge("abcabc", "abdcaba"), "abdcabcabcaba")
print(largestMerge("guguuuuuuuuuuuuuuguguuuuguug", "gguggggggguuggguugggggg"), "abdcabcabcaba")