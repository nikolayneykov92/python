from math import floor

time_first = int(input())
time_second = int(input())
time_third = int(input())

time_total = time_first + time_second + time_third
minutes = time_total / 60
seconds = time_total % 60

print(f"{floor(minutes)}:{seconds:02}")
