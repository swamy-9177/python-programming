n=int(input())
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print("perfect num")
else:
    print("not perfect number")
#example 6,28