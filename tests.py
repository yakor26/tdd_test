from check_pwd import check_pwd
import unittest

class TestCase(unittest.TestCase):
    def test1(self):
        input = "abcdefg"
        self.assertFalse(check_pwd(input))

if __name__ == "__main__":
    unittest.main()