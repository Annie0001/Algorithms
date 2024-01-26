# Convert this recurisve function sum_digits to an iterative function.

# def sum_digits(n):
#     if n<=9:
#         return n
#     last_digit = n%10
#     return sum_digits(n//10)+last_digit

def sum_digits(n):
    if n<=9:
        return n
    results = 0
    while n > 9:
        result += n % 10
        n = n // 10
    return result + n

print(sum_digits(12))
