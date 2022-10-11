def getShiftedString(s: str, leftShifts: int, rightShifts: int) -> str:

    def left_shift():
        return s[leftShifts:] + s[0:leftShifts]

    def right_shift():
        return s[-rightShifts:] + s[:-rightShifts]

    if len(s) == 1:
        return s
    if leftShifts != len(s):
        s = left_shift()
    if rightShifts != len(s):
        s = right_shift()
    return s

if __name__ == '__main__':
    string = 'VIVEK'
    l = 4
    r = -2
    print(getShiftedString(s=string, leftShifts=l, rightShifts=r))



