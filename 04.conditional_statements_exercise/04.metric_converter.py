value = float(input())
unit_in = input()
unit_out = input()

if unit_in == "m":
    value *= 1000
elif unit_in == "cm":
    value *= 10

if unit_out == "m":
    print(f"{(value / 1000):.3f}")
elif unit_out == "cm":
    print(f"{(value / 10):.3f}")
elif unit_out == "mm":
    print(f"{value:.3f}")
