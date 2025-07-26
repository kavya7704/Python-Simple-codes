def lexicographically(s):

    l = []
    d = ""
    for i in range(0,len(s)):
        d = s[i] + s[:i] + s[i+1:]
        l.append(d)
    l.sort()
    return l[0]

print(lexicographically("banana"))
