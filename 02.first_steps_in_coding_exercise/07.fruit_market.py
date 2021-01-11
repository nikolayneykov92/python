straweberries_price = float(input())
bananas_count = float(input())
oranges_count = float(input())
raspberries_count = float(input())
strawberries_count = float(input())

total_price = strawberries_count * straweberries_price
total_price += bananas_count * (straweberries_price * 0.1)
total_price += oranges_count * (straweberries_price * 0.3)
total_price += raspberries_count * (straweberries_price * 0.5)

print(total_price)