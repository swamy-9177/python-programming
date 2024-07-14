n=int(input("enter no of student"))
m=int(input("enter no of subjects"))
d={}
for i in range(n):
    k=input("enter roll number")
    v={}
    for j in range(m):
        sub=input("enter subject name")
        marks=int(input("enter marks"))
        v[sub]=marks
    d[k]=v
for i in d:
    print(i,"=",d[i])