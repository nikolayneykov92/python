length = int(input())
width = int(input())
height = int(input())
occupied_percentage = float(input())

total_volume = length * width * height
water_volume = (total_volume * (1 - (occupied_percentage * 0.01))) / 1000

print(water_volume)