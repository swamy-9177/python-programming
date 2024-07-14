#write a python program to print the numbers which are not divisible by 6,7,8, in given range
n=int(input())
m=int(input())
for i in range(n,m+1):
    if i%6!=0 and i%7!=0 and i%8!=0:
        print(i)

i=n
while i