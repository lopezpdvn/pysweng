def permutation(s):
    _permutation(s, "")

def _permutation(s, prefix):
    if not s:
        print(prefix)
        return
    for i in range(len(s)):
        rem = s[0:i] + s[i+1:]
        _permutation(rem, prefix + s[i])

def isunique0(s):
    sl = sorted(s)

    for i in range(len(sl)-1):
        if sl[i] == sl[i+1]:
            return False

    return True

def isunique1(s):
    return len(s) == len(set(s))

def isunique2(s):
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1

    return all(count == 1 for count in counts.values())

def isunique3(s):
    i = j = 0
    n = len(s)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if s[i] == s[j]:
                return False

    return True

print(isunique3('aaaa'))
print(isunique3('abcdb'))
print(isunique3('abhfjd'))
