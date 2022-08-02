class WeekDayError(Exception):
    pass


class Weeker:
    weekdays = {1: 'Mon',
                2: 'Tue',
                3: 'Wed',
                4: 'Thu',
                5: 'Fri',
                6: 'Sat',
                7: 'Sun'
                }

    def __init__(self, day):
        self.__day = day

    def __str__(self):
        return self.__day

    def add_days(self, n):
        for num, days in self.weekdays.items():
            if self.__day in days:
                n += num
                print(num, n)
                if (n % 7) != 0:
                    day_num = n % 7
                else:
                    day_num = num + 1
                print(day_num)
                self.__day = self.weekdays[day_num]


    def subtract_days(self, n):
        for num, days in self.weekdays.items():
            if self.__day in days:
                n -= num
                if (n * -1) % 7 != 0:
                    day_num = (n * -1) % 7
                else:
                    day_num = num + 1
                print(day_num)
                self.__day = self.weekdays[day_num]

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(16)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
