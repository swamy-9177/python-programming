#n natural usuing recursion
def recur(n):
    if n<1:
        return 1
    else:
        recur(n-1)
       # print(n)
n=int(input())
recur(n)
