day = input()

isWeekend = day == 'Saturday' or day == 'Sunday'
isWorkingDay = day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday'

if isWeekend:
    print('Weekend')
elif isWorkingDay:
    print('Working day')
else:
    print('Error')
