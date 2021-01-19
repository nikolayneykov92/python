city = input()
sells = float(input())

commission = -1

if city == "Sofia":
    if 0 <= sells <= 500:
        commission = 0.05
    elif 500 < sells <= 1000:
        commission = 0.07
    elif 1000 < sells <= 10000:
        commission = 0.08
    elif 10000 < sells:
        commission = 0.12
elif city == "Varna":
    if 0 <= sells <= 500:
        commission = 0.045
    elif 500 < sells <= 1000:
        commission = 0.075
    elif 1000 < sells <= 10000:
        commission = 0.1
    elif 10000 < sells:
        commission = 0.13
elif city == "Plovdiv":
    if 0 <= sells <= 500:
        commission = 0.055
    elif 500 < sells <= 1000:
        commission = 0.08
    elif 1000 < sells <= 10000:
        commission = 0.12
    elif 10000 < sells:
        commission = 0.145

if commission == -1:
    print("error")
else:
    print(f"{(sells * commission):.2f}")
