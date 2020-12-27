# String Compression
"""
Time complexity of O(n + k^2)
n: length of the input string
k: number of character sequences (=number of string concatenations)
"""

import unittest

def string_compress(s):
    rep = 0
    compressed=''
    for i in range(len(s)):
        rep += 1
        if i+1>=len(s) or s[i] != s[i+1]:
                compressed += s[i] + str(rep)
                rep=0
    if compressed == '1'.join(s)+'1':
        return s
    else:
        return compressed



class Test(unittest.TestCase):
    data=[
        ('aabbbcccc', 'a2b3c4'),
        ('naarrrggggees', 'n1a2r3g4e2s1'),
        ('sade', 'sade')
    ]

    def test_string_compression(self):
        for case, ans in self.data:
            print(string_compress(case))
            assert string_compress(case) == ans

if __name__ == '__main__':
    unittest.main()
