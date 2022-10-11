import sys
from unittest import *


# Function to convert Numbers to words

class IntegerToWords(object):
    """

    Args:
        num: Input integer number
            e.g. Input is 10
                 Input is 105
    Returns:
        converts number to words
            e.g. Output is Ten
                 Output is A Hundred and Five

    """

    """
    Algo:
        Step1 : Accept the input number
        Step2 : Check the length of the number
            Step2.1 : if length of number == zero or less than zero, indicate not valid value
        step3: Check the min and max length of the string. 
            step3.1 : if the length of the number is more than 4, hint
            
    """

    # lists:
    less_than_20 = [
        "", "One", "Two", "Three", "Four", "Five", "Six",
        "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
        "Thirteen", "Fourteen", "Fifteen", "Sixteen", "SevenTeen",
        "Eighteen", "Nineteen"
    ]
    tens_10_s = [
        "", "Ten", "Twenty", "Thirty", "Forty", "Fifty",
        "Sixty", "Seventy", "Eighty", "Ninety"
    ]

    thousands_1000_or_greater = [
        "",
        "Thousand",
        "Million",
        "Billion",
        "Trillion"
    ]

    # number to words
    def number_to_words(self, num):

        if not isinstance(num, int):
            raise ValueError(f"{num} must be a integer")
        if num == 0 or num < 0:
            return "Number is zero or less"

        ans = ""

        i = 0
        while num > 0:
            if num % 1000 != 0:
                ans = self.helper(num % 1000) + IntegerToWords.thousands_1000_or_greater[i] + " " + ans
                i += 1
                num //= 1000
            return ans.strip()

    def helper(self, n):
        if not isinstance(n, int):
            raise ValueError(f"{n} must be an integer")
        if n == 0:
            return ""
        elif n < 20:
            return IntegerToWords.less_than_20[n] + " "
        elif n < 100:
            return IntegerToWords.tens_10_s[n // 10] + " " + self.helper(n % 10)
        else:
            return IntegerToWords.less_than_20[n // 100] + " Hundred " + self.helper(n % 100)


def integer_to_words(num):
    # define a dictionary zero to ninety
    d = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
         6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
         11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
         15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
         19: 'nineteen', 20: 'twenty',
         30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
         70: 'seventy', 80: 'eighty', 90: 'ninety'}
    k = 1000    # `k` = thousands
    m = k * 1000  # `m` = million
    b = m * 1000  # `b` = billion
    t = b * 1000  # `t' = trillion

    assert(0 <= num)
    if num < 20:
        return d[num]
    if num < 100:
        if num % 10 == 0:
            return d[num]
        else:
            return d[num // 10 * 10] + '-' + d[num % 10]
    if num < k:
        if num % 100 == 0:
            return d[num // 100] + ' hundred '
        else:
            return d[num // 100] + ' hundred and ' + \
                   integer_to_words(num % 100)
    if num < m:
        if num % k == 0:
            return integer_to_words(num // k) + 'thousand'
        else:
            return integer_to_words(num // k) + ' thousand and, ' + \
                   integer_to_words(num % k)

    if num < b:
        if num % m == 0:
            return integer_to_words(num // m) + ' million'
        else:
            return integer_to_words(num // m) + ' million, ' + \
                   integer_to_words(num % m)

    if num < t:
        if num % t == 0:
            return integer_to_words(num // b) + ' billion'
        else:
            return integer_to_words(num // b) + ' billion, ' + \
                   integer_to_words(num % b)

    if num % t == 0:
        return integer_to_words(num // t) + ' trillion'
    else:
        return integer_to_words(num // t) + ' trillion, ' + \
               integer_to_words(num % t)
    raise AssertionError('Number is too large: %s' % str(num))


if __name__ == "__main__":

    i2e = IntegerToWords()

    numbers_for_testing = [
        1, -9, 10, 19, 11, 22, 40, 55, 99, 100, 101,
        102, 150,
        512, 1004, 100000, 1111100000
    ]

    # for number in numbers_for_testing:
        # print(i2e.number_to_words(number))


    numbers_testing = [
        1, 10, 19, 11, 22, 40, 55, 99, 100, 101,
        102, 150,
        512, 1004, 100000, 1111100000
    ]

    for n in numbers_testing:
        print(integer_to_words(n))



