'''n=int(input())
count=0
for i in range(2,n):
    if(n%i==0):
        count+=1
if count==1:
    print("prime")

else:
    print("not prime")'''
'''n=int(input())
for i in  range(2,(n//2)+1):
    if n%i==0:
        print("not prime")
        break
else:
    print("prime")'''
n=int(input())
for i in  range(2,(n**0.5)+1):
    if n%i==0:
        print("not prime")
        break
else:
    print("prime")



