import unittest


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.g = globals()

    def test_a(self):
        # 假设这个是这个接口的返回值
        return_valueA = {'code': 1}
        print(f'这个接口返回为{return_valueA}')

        # 这里使用globals()
        # A接口的返回值
        self.g['a'] = return_valueA

    def test_b(self):
        # 假设这个接口要用这个data
        # B接口需要用到A接口的返回值
        print(f'这里是需要用到的test_b的返回值的函数:%s' % self.g['a'])

        # 假设他是b接口的返回值
        return_valueB = {'messge': "ok"}
        # 直接用globals()赋值就ok了
        self.g['b'] = return_valueB

    def test_c(self):
        # 假设这个是C接口，需要用到B接口的返回值

        print(f'这里是需要用到的test_b的返回值的函数:%s' % self.g['b'])


if __name__ == '__main__':
    unittest.main()
