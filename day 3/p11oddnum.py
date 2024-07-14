l=map(int(input().split()))
l1=[]
for i in l:
    if i%2!=0:
        l1[i]=l[i]
print(l1.sum())
        