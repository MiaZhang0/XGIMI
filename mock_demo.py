import unittest
from unittest import mock


class SubClass(object):
    def add(self, a, b):
        pass


class TestSub(unittest.TestCase):
    def test_sub(self):
        sub = SubClass()  # 实例化对象
        sub.add = mock.Mock(return_value=10)  # mock add方法 返回10
        result = sub.add(5, 5)  # 调用被测函数
        self.assertEqual(result, 10)  # 断言实际结果和预期结果


if __name__ == '__main__':
    unittest.main()
