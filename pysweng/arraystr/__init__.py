def permutation(s):
    _permutation(s, "")

def _permutation(s, prefix):
    if not s:
        print(prefix)
        return
    for i in range(len(s)):
        rem = s[0:i] + s[i+1:]
        _permutation(rem, prefix + s[i])
