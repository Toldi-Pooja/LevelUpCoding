def sum_of_digits(num):
    if num == 0:
        return 0
    total = 0
    n = abs(num)
    while n > 0:
        last_digit = n % 10
        total = total+last_digit 
        n = n//10
    return total
n = int(input("Enter the number: "))
print(sum_of_digits(n))