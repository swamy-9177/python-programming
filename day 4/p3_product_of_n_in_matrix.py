r,c=int(input("rows")),int(input("columns"))
l=[]#l=[0]*r
for i in range(r):
    l.append(list(map(int,input().split())))#l[i]=list(map(int,input().split()))
print(l)
product=1
for i in l:
     for j in i:
          print(j)
          product*=j
print(product)
