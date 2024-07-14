s=input()
s1=""
for i in s:
    if i in "aeiouAEIOU":
        if s.count(i)%2!=0:
            s1+=i
print((s1[0]+" "+s1[1]))
