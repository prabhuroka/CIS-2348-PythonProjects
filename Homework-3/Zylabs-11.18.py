# Prabhu Roka
# 1986444
numbers = input().split()

non_negative_numbers = [int(num) for num in numbers if int(num) >= 0]

non_negative_numbers.sort()

for num in non_negative_numbers:
    print(num, end=" ")
