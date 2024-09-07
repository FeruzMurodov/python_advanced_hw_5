def substrings(s: str):
    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            yield s[start:end]


s = 'abrakadabra'
print(*substrings(s))
