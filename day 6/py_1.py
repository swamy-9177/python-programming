'''discount for men :5%
   discount for women:7%
   discount on each item:3*no of items
   calculate total bill
   take items and their prices in runtime
   '''
n=int(input("Enter no of Items"))
d={}
for i in range(n):
    k=input("enter items")
    v=int(input("Enter items price"))
    d[k]=v
l=[]
for i in d:
    l.append(d[i]-d[i]*(3*n)/100)
g=input("enter gender :")
if g=="MALE":
    bill=sum(l)-sum(l)*5/100
else:
    bill=sum(l)-sum(l)*7/100
j=0
print("items - price :discount-prices")
for i  in d:
    print(f"{i}-{d[i]}:{l[j]}")
    j+=1
else:
    print("*"*20)
    print("Thank you visit again")
print(f"total bill : {bill}")
