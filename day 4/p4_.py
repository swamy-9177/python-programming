#sum of maximum  and min element in a matrix in  tu
r,c=int(input("rows")),int(input("columns"))
l=[]
for i in range(r):
    l.append(tuple(map(int,input().split())))
min,max=1000,0
print(tuple(l))
for i in l:
    print(i)
    for j in i:
        if j>max:
            max=j
        if j<min:
            min=j
print("minimum element",min)
print("maximum element",max)
print(max+min)
