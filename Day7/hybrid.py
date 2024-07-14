def superReducedString(s):
    s = list(s)
    while 1:
        if len(s) == 0:
            return 'Empty String'
        if len(s) == 1:
            return s[0]
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                del s[i]
                del s[i-1]
                break
            if i == (len(s) - 1):
                return ''.join(s)
a=input()
b=superReducedString(a)
print(b)