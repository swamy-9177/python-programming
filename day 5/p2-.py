n=int(input())
d=()
for i  in range(n):
    k,v=map(str,input().split())
    d[k]=v
m=int(input("no of serarch elements"))
for i in range(m):
    s=input()
    if s in d:
        print(s,d[s])
    else:
        print("swami")
