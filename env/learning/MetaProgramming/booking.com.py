

import math
import os
import random
import re
import sys


#
# Complete the 'awardTopKHotels' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING positiveKeywords
#  2. STRING negativeKeywords
#  3. INTEGER_ARRAY hotelIds
#  4. STRING_ARRAY reviews
#  5. INTEGER k
#

def awardTopKHotels(positiveKeywords, negativeKeywords, hotelIds, reviews, k):
    # Write your code here
    words_positive = set()
    words_negative = set()

    # Positive wordings
    for word in positiveKeywords.split(" "):
        words_positive.add(word.lower())

    # Negative wordings
    for word in negativeKeywords.split(" "):
        words_negative.add(word.lower())

    # Instantiate hotel scoring
    hotel_scores = {}

    # lets give score based on the review
    for item in range(0, len(reviews)):

        hotel = hotelIds[item]
        score = hotel_scores.get(hotel, 0)
        review = reviews[item].split(" ")

        positive = 0
        negative = 0

        for word in review:
            if word[-1] == '.' or word[-1] == ',':
                word = word[0:-1]

            # positive reviews
            if word.lower() in words_positive:
                positive += 1

            # Negative reviews
            if word.lower() in words_negative:
                negative += 1

        # scoring
        hotel_scores[hotel] = score + 3 * positive - negative

    # results
    result = sorted(hotel_scores, key=hotel_scores.get, reverse=True)

    return result[0:k]

# Beautiful Subarrays
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'beautifulSubarrays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER numOdds
#

def beautifulSubarrays(arr, numOdds):
    # Write your code here
    c = 0  # count of odds
    odds = 0  # odds
    p = [0] * (len(arr) + 1)

    for elem in range(len(arr)):
        p[odds] += 1

        # elements of array if odd
        if arr[elem] & 1:
            odds += 1

        # odd elements greater or equal to numOdds
        if odds >= numOdds:
            c += p[odds - numOdds]

    return c


# Shifting Strings


import math
import os
import random
import re
import sys


#
# Complete the 'getShiftedString' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER leftShifts
#  3. INTEGER rightShifts
#

def getShiftedString(s, leftShifts, rightShifts):
    # left shift - algo
    def left_Shift(string):
        first_character = string[0]
        rest_of_string_left = string[1:]
        return rest_of_string_left + first_character

    # right shift - algo
    def right_Shift(string):
        last_character = string[-1]
        rest_of_string_right = string[:-1]
        return last_character + rest_of_string_right

    if len(s) == 1:
        return s

    if leftShifts != len(s):
        for alpha in range(0, leftShifts):
            s = left_Shift(s)

    if rightShifts != len(s):
        for alpha in range(0, rightShifts):
            s = right_Shift(s)

    return s


