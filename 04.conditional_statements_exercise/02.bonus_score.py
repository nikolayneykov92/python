number = int(input())
bonus = 0

if number <= 100:
    bonus = 5
elif number > 100 and number <= 1000:
    bonus = number * 0.2
elif number > 1000:
    bonus = number * 0.1

bonus += 1 if number % 2 == 0 else 2 if number % 5 == 0 else 0

print(bonus)
print(number + bonus)