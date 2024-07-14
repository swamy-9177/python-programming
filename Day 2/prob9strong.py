#strong number 145 sum 0f individual def strongnum(n):
'''def fact(n):
    if n==0:
        return 1
    else:
        '''

'''def strong(n):
    x,sum=n,0
    while n>0:
        digit=n%10
        fact=1
        for i in range(1,digit+1):
            fact*=i
        sum+=fact
        n//10
    if sum==x:
        return "strong numbeer"
    else:
        return "Not a strong number"
n=int(input(int()))
print(strong(n))
        '''
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def is_strong_number(n):
    original_number = n
    digit_sum = 0

    while n > 0:
        digit = n % 10
        digit_sum += factorial(digit)
        n //= 10

    return original_number == digit_sum

# Example usage
number_to_check = int(input("Enter a number to check if it's a strong number: "))
if is_strong_number(number_to_check):
    print(f"{number_to_check} is a strong number.")
else:
    print(f"{number_to_check} is not a strong number.")


