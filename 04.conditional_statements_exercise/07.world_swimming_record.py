from math import floor

record_seconds = float(input())
distance_meters = float(input())
seconds_per_meter = float(input())

time_result = (distance_meters * seconds_per_meter) + floor(distance_meters / 15) * 12.5

if record_seconds > time_result:
    print(f"Yes, he succeeded! The new world record is {time_result:.2f} seconds.")
else:
    print(f"No, he failed! He was {(time_result - record_seconds):.2f} seconds slower.")
