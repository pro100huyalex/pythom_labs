from collections import Counter

def count_freq(tokens: list[str]) -> dict[str, int]:
    return dict(Counter(tokens))
print(count_freq(["a","b","a","c","b","a"]))