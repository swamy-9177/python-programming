#write 
n=int(input())
d={}
for i in range(n):
    key=input("key:")
    value=input("value")
    d[key]=value
for i in d:
     print(f"key: {i} value : {d[i]}")
     print("key:{} value: {}".format({i,d[i]}))
for i in d.keys():
    print(i)
for i in d.values():
    print(i)
     
