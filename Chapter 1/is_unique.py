# Dec. 15, 2020
# Author: Arian Nsz

"""
What are the assumptions?
we can assume ASCII which leads to 128 unique characters (our assumption here)

Extended ASCII : 256 characters

Unicode 2^(21) characters
"""
import unittest


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

def pytonic_is_unique(s):
    return len(set(s)) == len(s)

class Test(unittest.TestCase):
    test_cases=[
    ('abcdef', True),
    ('aaa', False),
    ('123456789010', False),
    ('arges', True)
    ]

    test_functions = [is_unique, pytonic_is_unique]

    def test_is_unique(self):
        for function in self.test_functions:
            for txt, expected in self.test_cases:
                assert function(txt)==expected


if __name__ == '__main__':
    unittest.main()
