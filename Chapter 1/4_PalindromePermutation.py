# Palindrome Permutation
import unittest

def parlindorme(s):
    dic={}
    for char in s:
        if char in dic:
            dic[char] +=1
        else:
            dic[char] = 1
    flag = 0
    for char in dic:
        if dic[char]%2 != 0 :
            flag +=1
        if flag==2:
            return False
    return True



class Test(unittest.TestCase):
    data=[
        ("tactcoa", True),
        # ("Tact Coa", False),
        ("aarriiaan", True),
        ('python', False)
    ]

    def test_pal(self):
        for case, ans in self.data:
            print('expected ' + str(ans))
            print('answer is ' + str(parlindorme(case)))
            assert parlindorme(case)== ans

if __name__ == '__main__':
    unittest.main()
