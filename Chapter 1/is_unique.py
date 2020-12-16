# Dec. 15, 2020
# Author: Arian Nsz

"""
What are the assumptions?
we can assume ASCII which leads to 128 unique characters (our assumption here)

Extended ASCII : 256 characters

Unicode 2^(21) characters
"""
import unittest



"""
# First solution
it can be seen as either O(N) when length of the string is less than 128
or we can argue O(1), because it won't exceed 128 iterations.
"""
def is_unique(s):
    if len(s)>128:
        return False
    else:
        d={}
        for c in s:
            if c in d:
                return False
            else:
                d[c]= True
        return True



"""
# 2nd Solution
"""
def pytonic_is_unique(s):
    return len(set(s)) == len(s)


"""
# 3rd Solution
O(N^2)
"""
def noTemp_is_unique(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False
    return True



"""
# 4th solution
O(N logN )
"""
def sort_is_unique(s):
    s = sorted(s)
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            return False
    return True



class Test(unittest.TestCase):
    test_cases=[
    ('abcdef', True),
    ('aaa', False),
    ('123456789010', False),
    ('arges', True)
    ]

    test_functions = [is_unique, pytonic_is_unique, noTemp_is_unique, sort_is_unique]

    def test_is_unique(self):
        for function in self.test_functions:
            for txt, expected in self.test_cases:
                assert function(txt)==expected


if __name__ == '__main__':
    unittest.main()
