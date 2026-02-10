def count_digits(num):
    if num == 0:
        return 1
    count = 0
    n = abs(num)
    while n > 0:
        last_digit = n % 10
        count += 1
        n = n//10
    return count
n = int(input("Enter the number: "))
print(count_digits(n))