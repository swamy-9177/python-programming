l,d=map(int,input().split())
list=list(map(int,input().split()))
for i in list:
    for j in list:
        if i-j==d:
            flag=1
if flag==1:
    print(True)
else:
    print(False)

print(list)

 


