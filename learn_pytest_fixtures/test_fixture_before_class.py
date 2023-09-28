import pytest


class TestFixturesScope:

    # the scope is set to class
    # the fixture will be executed before all the test methods
    @pytest.fixture(scope='class', autouse=True)
    def setup(self):
        print("\n setup fixture is called - class level")

    def test_method1(self):
        print("method1 is executed")

    def test_method2(self):
        print("method2 is executed")

    def test_method3(self):
        print("method3 is executed")
