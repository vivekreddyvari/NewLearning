import os.path, time
from stat import ST_CTIME, ST_SIZE, ST_MTIME
from datetime import datetime
from dateutil.relativedelta import relativedelta


def findNumber(arr, k):
    for elem in arr:
        if elem == k:
            print("Yes")
        else:
            print("No")


def oddNumbers(l, r):
    number_range = range(l, r)
    for num in number_range:
        if num % 2 != 0:
            print(num)


class Solution(object):

    def backspaceCompare(self, S, T):
        def build(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(S) == build(T)


def minimumBribes(q):
    i = 0
    for element in q:
        print(element, q[0:element])


def back_space_solution(s: str) -> str:
    s_list = list(s)
    s_out = [] # Single Character string output : List (type)
    string_out = "" # string output
    for element in range(len(s_list)):
        if s_list[element] != '#':
            s_out.append(s_list[element])
        if s_list[element] == "#" and len(s_out) > 0:
            s_out.pop()

    return string_out.join(map(str, s_out))


def name_the_set(path):
    name_set = set()
    for file in os.listdir(path):
        fullpath = os.path.join(path, file)
        if os.path.isfile(fullpath):
            name_set.add(file)
    return name_set


def retrieved_set(name_set, path):
    retrieved_set_file = set()
    for name in name_set:
        stat = os.stat(os.path.join(path, name))
        time = datetime.fromtimestamp(stat[ST_CTIME])
        # print(name, datetime.fromtimestamp(stat[ST_CTIME]))
        retrieved_set_file.add((time, name))
    return retrieved_set_file

if __name__ == '__main__':
    # arr = [1,3,4,5,6,7]
    # findNumber(arr=arr, k=4)
    # Test01
    # l = 2
    # r = 10
    # oddNumbers(l, r)
    # test02
    # q = [1,2,4,3]
    # print(minimumBribes(q))

    strings = ["adbce#vb##ff", "ade#vb###ff", "ace###f", "##04###04" ]
    for string in strings:
        print(back_space_solution(s=string))

    # latest files
    savedSet = set()
    mypath = "../../learning/MetaProgramming"

    name_set = name_the_set(path=mypath)
    retrieved_set = retrieved_set(name_set=name_set, path=mypath)
    # print(type(retrieved_set))
    retrieved_set = sorted(retrieved_set, reverse=True)
    for obj in retrieved_set:
        date_time_now = datetime.today()
        only_30 = date_time_now - relativedelta(minutes=30)
        # print(only_30) pr
        if obj[0] >= only_30:
            print(str(obj[0]) + ' ' + obj[1])



# talk