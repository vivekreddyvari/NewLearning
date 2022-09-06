import pdb
# pdb.set_trace()


class Reverse:
    """ This snippet return the reverse of string"""

    def reverse_left(self, string: str, d: int):
        """ Reverse string from left """
        self.string = string
        self.d = d

        tmp = self.string[self.d:] + self.string[0: self.d]
        return tmp

    def reverse_right(self):
        """ Reverse string from right """
        tmp = self.reverse_left(self.string, len(self.string) - self.d)
        return tmp

rev_string = Reverse()

# reverse
string = "Vivek"
d = 2

print(f"Left Reverse = {rev_string.reverse_left(string=string, d=d)}")
print(f"Right Reverse = {rev_string.reverse_right()}")
