def fact(n):
    if n<1:
        return 1
    else:
        return n*fact(n-1)
def strong(x):
    s=str(x)
    sum=0
    for i in s:
        sum+=fact(int(i))
    if sum==x:
        print(x)
a,b=int(input()),int(input())
for i in range(a,b+1):
    strong(i)
