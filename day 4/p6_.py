#write a python program   to print sum of elements in last row of list
r,c=int(input("rows")),int(input("columns"))
l,sum=[],0
for i in range(r):
    l.append(tuple(map(int,input().split())))
for i in l:
     sum+=i[-1]
print(sum)
       