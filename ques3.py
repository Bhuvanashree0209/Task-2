def is_happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

numbers = [10, 501, 22, 37, 100, 999, 87, 351]
happy_numbers_count = 0

for num in numbers:
    if is_happy_number(num):
        happy_numbers_count += 1

print("Number of happy numbers:", happy_numbers_count)
