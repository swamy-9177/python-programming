'''class Factorial:
    def fact(self,n):
         self.n=n
         f=1
         for i in range(1,n+1):
              f*=i
         print(f)
obj=Factorial()
obj.fact(int(input()))'''
'''class Factorial:
    def fact(self,n):
         return n*fact(n-1)
         print(n)
obj=Factorial()
obj.fact(int(input()))'''
class Factorial:
    def __init__(self,data):
         self.data=data
         self.fact(data)
    def fact(self,n):
         self.n=n
         f=1
         for i in range(1,n+1):
              f*=i
         print(f)
obj=Factorial(int(input()))



    

