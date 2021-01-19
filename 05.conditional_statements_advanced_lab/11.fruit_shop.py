fruit = input()
day = input()
quantity = float(input())

is_weekend = day == "Saturday" or day == "Sunday"
is_working_day = day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday"

fruit_price = -1

if fruit == "banana":
    if is_working_day:
        fruit_price = 2.50
    elif is_weekend:
        fruit_price = 2.70
elif fruit == "apple":
    if is_working_day:
        fruit_price = 1.20
    elif is_weekend:
        fruit_price = 1.25
elif fruit == "orange":
    if is_working_day:
        fruit_price = 0.85
    elif is_weekend:
        fruit_price = 0.90
elif fruit == "grapefruit":
    if is_working_day:
        fruit_price = 1.45
    elif is_weekend:
        fruit_price = 1.60
elif fruit == "kiwi":
    if is_working_day:
        fruit_price = 2.70
    elif is_weekend:
        fruit_price = 3.00
elif fruit == "pineapple":
    if is_working_day:
        fruit_price = 5.50
    elif is_weekend:
        fruit_price = 5.60
elif fruit == "grapes":
    if is_working_day:
        fruit_price = 3.85
    elif is_weekend:
        fruit_price = 4.20

print("error" if fruit_price == -1 else f"{(quantity * fruit_price):.2f}")
