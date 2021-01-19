movie_budget = float(input())
supernumerary_count = int(input())
supernumerary_cloth_price = float(input())

decor_price = movie_budget * 0.1
supernumerary_price = supernumerary_count * supernumerary_cloth_price

if supernumerary_count > 150:
    supernumerary_price *= 0.9

total_price = decor_price + supernumerary_price

movie_budget -= total_price

if movie_budget >= 0:
    print("Action!")
    print(f"Wingard starts filming with {movie_budget:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {abs(movie_budget):.2f} leva more.")
