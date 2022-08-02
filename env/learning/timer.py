class Timer:
    """ Timer to """
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __str__(self):
        self.time_hhmmss = "%02d:%02d:%02d" % (self.__hour, self.__minute, self.__second)
        return self.time_hhmmss

    def next_second(self):
        if self.__second == 59 and self.__minute == 59 and self.__hour <= 23:
            self.__second = 0
            self.__minute = 0
            self.__hour = 0
        else:
            self.__second += 1

    def prev_second(self):
        if self.__hour == 0 and self.__minute == 0 and self.__second == 0:
            self.__hour = 23
            self.__minute = 59
            self.__second = 59
        else:
            self.__second -= 1




timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print("next second", timer)
timer.prev_second()
print("previous second", timer)

