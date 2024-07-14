#write a python program to print sum of n matrix
r,c=int(input("rows")),int(input("columns"))
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
print(l)
sumn=0
for i in l:
    print(i)
    sumn+=sum(i)
print(sumn)

    


