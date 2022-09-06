

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

if __name__ == '__main__':
    # arr = [1,3,4,5,6,7]
    # findNumber(arr=arr, k=4)
    l = 2
    r = 10
    oddNumbers(l, r)
