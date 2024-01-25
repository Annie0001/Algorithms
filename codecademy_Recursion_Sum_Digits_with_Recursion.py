def sum_digits(n): 
    if n <= 9: 
        return n 
    last_digit = n % 10 
    return sum_digits(n // 10) + last_digit

print(sum_digits(552))