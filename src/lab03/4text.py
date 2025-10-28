def top(a: list):
    prow = set(a)
    prow = sorted(a)
    schet = {}
    for i in prow:
        schet[i] = a.count(i)
    return schet
print(top(["bb", "aa", "bb", "aa", "cc" ]))