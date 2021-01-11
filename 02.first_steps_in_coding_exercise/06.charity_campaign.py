days = int(input())
cooks = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())

cakes_price = cakes * 45
waffles_price = waffles * 5.8
pancakes_price = pancakes * 3.2

total_price = (cakes_price + waffles_price + pancakes_price) * cooks * days * 0.875

print(total_price)
