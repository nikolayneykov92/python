product = input()
city = input()
quantity = float(input())

price = 0

if product == "coffee":
    if city == "Sofia":
        price = 0.5 * quantity
    elif city == "Plovdiv":
        price = 0.4 * quantity
    elif city == "Varna":
        price = 0.45 * quantity
elif product == "water":
    if city == "Sofia":
        price = 0.8 * quantity
    elif city == "Plovdiv":
        price = 0.7 * quantity
    elif city == "Varna":
        price = 0.7 * quantity
elif product == "beer":
    if city == "Sofia":
        price = 1.2 * quantity
    elif city == "Plovdiv":
        price = 1.15 * quantity
    elif city == "Varna":
        price = 1.10 * quantity
elif product == "sweets":
    if city == "Sofia":
        price = 1.45 * quantity
    elif city == "Plovdiv":
        price = 1.30 * quantity
    elif city == "Varna":
        price = 1.35 * quantity
elif product == "peanuts":
    if city == "Sofia":
        price = 1.60 * quantity
    elif city == "Plovdiv":
        price = 1.50 * quantity
    elif city == "Varna":
        price = 1.55 * quantity

print(price)
