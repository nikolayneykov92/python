vacation_price = float(input())
puzzle_count = int(input())
doll_count = int(input())
bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

wonned_money = puzzle_count * 2.6 + doll_count * 3 + bear_count * 4.1 + minion_count * 8.2 + truck_count * 2
total_toy_count = puzzle_count + doll_count + bear_count + minion_count + truck_count

if total_toy_count >= 50:
    wonned_money *= 0.75

wonned_money *= 0.9

money_diff = wonned_money - vacation_price

if money_diff >= 0:
    print(f"Yes! {money_diff:.2f} lv left.")
else:
    print(f"Not enough money! {abs(money_diff):.2f} lv needed.")
