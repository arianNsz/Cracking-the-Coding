# One Away
"""
"""

import unittest

def one_away(s1, s2):
    if s1==s2:
        return True
    elif (len(s1) - len(s2))==1:
        return one_edit(s1, s2)
        # return one_diff_check(s1, s2)
    elif (len(s2) - len(s1))==1:
        return one_edit(s2, s1)
        # return one_diff_check(s1, s2)
    elif len(s1) == len(s2):
        # return one_edit(s1, s2)
        return replace_check(s1, s2)
    else:
        return False


def one_diff_check(long_string, short_string):
    for i in range(len(long_string)):
        if long_string[:i] + long_string[i+1:] == short_string:
            return True
    return False




def one_edit(long_string, short_string):
    i, j = 0, 0
    flag = False
    while i<len(long_string) and j<len(short_string):
        if short_string[j] != long_string[i]:
            if flag:
                return False
            flag = True
            i += 1
        else:
            i += 1
            j += 1
    return True





def replace_check(s1, s2):
    missmatch_flag= False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if missmatch_flag:
                return False
            missmatch_flag = True
    return True


class Test(unittest.TestCase):
    data = [
        ('apple', 'apple', True),
        ('apple', 'able', False),
        ('apple', 'aple', True)
    ]

    def test(self):
        for s1, s2, ans in self.data:
            assert one_away(s1, s2) == ans

if __name__ == '__main__':
    unittest.main()
