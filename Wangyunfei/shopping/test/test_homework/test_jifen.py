import unittest
from Wangyunfei.shopping.test.test_homework.shopping import memberHelp

class MyTestCase(unittest.TestCase):
    def test_jifen(self):
        exp = 0.9
        act = memberHelp.Cumulative_members_jifen(18812345673, 2000)
        self.assertEqual(act, exp)


if __name__ == '__main__':
    unittest.main()
