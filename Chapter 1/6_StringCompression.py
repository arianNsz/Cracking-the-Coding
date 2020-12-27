# String Compression
"""
Time complexity of O(?)
"""

import unittest

def string_compress(s):
    char=[]
    num=[]
    i, j = 1, 0
    rep=1
    while i<len(s):
        if s[j] == s[i]:
            rep += 1
            if i < len(s)-1 :
                i += 1
            else:
                num.append(rep)
                char.append(s[j])
                break
        else:
            num.append(rep)
            char.append(s[j])
            j = i
            if i < len(s)-1 :
                i += 1
            else:
                num.append(1)
                char.append(s[-1])
                break
            rep =1
    ans=''

    if sum(num) == len(num):
        return s
    else:
        for i in range(len(char)):
            ans += char[i]+str(num[i])
        return ans





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
