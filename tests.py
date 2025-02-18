from check_pwd import check_pwd
import unittest

class TestCase(unittest.TestCase):
    def test1(self):
        input = "abcdefg"
        self.assertFalse(check_pwd(input))
    
    def test2(self):
        input = "abcdefgabcdefgabcdefg"
        self.assertFalse(check_pwd(input))
    
    def test3(self):
        input = "123ABC#@"
        self.assertFalse(check_pwd(input))
    
    def test4(self):
        input = "123abc#@"
        self.assertFalse(check_pwd(input))
    
    def test5(self):
        input = "ABCabc#@"
        self.assertFalse(check_pwd(input))

if __name__ == "__main__":
    unittest.main()