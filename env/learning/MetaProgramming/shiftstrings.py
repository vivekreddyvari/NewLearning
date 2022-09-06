def getShiftedString(s: str, leftShifts: int, rightShifts: int) -> str:

    def left_shift():
        return s[leftShifts:] + s[0:leftShifts]

    def right_shift():
        return s[-rightShifts:] + s[:-rightShifts]

    if len(s) == 1:
        return s
    for n in range(0, leftShifts):
        if leftShifts != len(s):
            s = left_shift()
    for n in range(0, rightShifts):
        if rightShifts != len(s):
            s = right_shift()
    return s

if __name__ == '__main__':
    string = 'VIVEK'
    l = 0
    r = 3
    print(getShiftedString(s=string, leftShifts=l, rightShifts=r))



