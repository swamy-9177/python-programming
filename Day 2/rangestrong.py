'''def stronginrange(n,m):
    for i in range(n,m+1):
        x,sum=i,0
        while i>0:
            digit=i%10
            fact=1
            for j  in range(1,digit+1):
                fact*=j
            sum+=fact
            i//10
        if sum==x:
            print(x)
n,m=int(input()),int(input())
stronginrange(n,m)'''
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

def find_strong_numbers_in_range(start, end):
    strong_numbers = []
    for num in range(start, end + 1):
        if is_strong_number(num):
            strong_numbers.append(num)
    return strong_numbers

# Example usage
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

result = find_strong_numbers_in_range(start_range, end_range)

if result:
    print(f"Strong numbers in the range {start_range} to {end_range}: {result}")
else:
    print(f"There are no strong numbers in the range {start_range} to {end_range}.")
