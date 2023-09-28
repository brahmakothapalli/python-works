import pytest


class TestFixturesScope:

    # by default the scope is function
    @pytest.fixture(autouse=True)
    def setup(self, request):
        print("setup fixture is called")

        def tear_down():
            print("closing the browser")
        request.addfinalizer(tear_down)

    def test_method1(self):
        print("method4 is executed")

    def test_method2(self):
        print("method5 is executed")

    def test_method3(self):
        print("method6 is executed")
