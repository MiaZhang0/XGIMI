import pytest


class Test_Case():
    def setup_class(self):
        print("------->setup_class")

    def teardown_class(self):
        print("------->teardown_class")

    def test_a(self):
        print("")
        assert 1


if __name__ == '__main__':
    if __name__ == '__main__':
        pytest.main("-s test_case.py")
