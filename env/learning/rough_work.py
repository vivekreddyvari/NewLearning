weekdays = {1: 'Mon',
            2: 'Tue',
            3: 'Wed',
            4: 'Thu',
            5: 'Fri',
            6: 'Sat',
            7: 'Sun'
            }


print("Negative")
day = 'Tue'
n = 23

for num, days in weekdays.items():
    if day in days:
        n -= num
        print(n, num, end='\n\n' )

        if (n * -1) % 7 != 0:
            day_num = (n * -1) % 7
            print(day_num)
        else:
            day_num = num + 1
            print(day_num)

print(weekdays[day_num], "subtract")