#write a python program to do encrption and decryption with  kay values with functi
def encryption(s,k):
    s1=""
    for i in s:
        x=ord(i)+k
        s1+=chr(x)
    print(s1)
def decryption(s,k):
    s1=""
    for i in s:
        x=ord(i)-k
        s1+=chr(x)
    print(s1)
k=int(input("enter key value:"))
s=input("Enter the string")
op=input("select operation:")
if op=="encrypt":
    encryption(s,k)
elif op=="decrypt":
    decryption(s,k)
else:
    print("inappropiate")
    