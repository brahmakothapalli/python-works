import pytest


class TestFixturesScope:

    # by default the scope is function
    @pytest.fixture(autouse=True)
    def setup(self):
        print("setup fixture is called")

    def test_method1(self):
        print("method4 is executed")

    def test_method2(self):
        print("method5 is executed")

    def test_method3(self):
        print("method6 is executed")
