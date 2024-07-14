def recur(n):
    sum=0
    if n<1:
        return 1
    else:
        return n+recur(n-1)
n=int(input())
sum=recur(n)
print(sum)
