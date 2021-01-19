day = input()

is_weekend = day == "Saturday" or day == "Sunday"
is_working_day = day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday"

if is_weekend:
    print("Weekend")
elif is_working_day:
    print("Working day")
else:
    print("Error")
