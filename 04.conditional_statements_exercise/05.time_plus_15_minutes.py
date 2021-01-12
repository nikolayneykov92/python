from math import floor

hour = int(input())
minutes = int(input())

hour = (hour + floor((minutes + 15) / 60)) % 24
minutes = (minutes + 15) % 60

print(f'{hour}:{minutes:02}')
