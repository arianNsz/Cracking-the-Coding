# Question 1.3: URLify

import unittest

def urlify(s):
    list_s = s.split()
    ans = "20%".join(list_s)
    return ans

class Test(unittest.TestCase):
    test_cases=[
    ("arian   narges married          ", "arian20%narges20%married"),
    ("hello world          dear   computer    ", "hello20%world20%dear20%computer" )
    ]

    def tester(self):
        for case, ans in self.test_cases:
            assert urlify(case)==ans

if __name__ == '__main__':
    unittest.main()
