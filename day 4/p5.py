r,c=int(input("rows")),int(input("columns"))
l,sum=[],0
for i in range(r):
    l.append(tuple(map(int,input().split())))
for i in l:
    print(i)
    for j in i:
        sum+=j
print(sum/(r*c))
       