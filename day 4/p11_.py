#print vowel count and vowels in string
'''s=input()
s1=""
count=0
for i in s:
    if s in "a"or"e"or"i"or"u":
        s1=s
        count+=1
print(count)
print(s1)
'''
def counting(s):
    print(s)
    s1,vc='',0
    for i in s:
        if i in "aeiouAEIOU":
            vc+=1
            s1+=i
    print("Vowel count:",vc)
    print(list(set(s1)))
l=input().split()
for i in l:
    counting(i)





