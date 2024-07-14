def comp_or_prime(m):
    for i in  range(2,m):
        if m%i==0:
            return "composite"
    else:
        return "prime"
n=int(input())
d={}
for i in range(n):
    k=i+1
    v=comp_or_prime(i+1)
    d[k]=v
print(d)

