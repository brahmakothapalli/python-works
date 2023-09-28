import pytest


class TestParametrization:

    @pytest.mark.parametrize("name", ["John", "David"])
    def test_say_hello(self, name):
        print(f"Hello!! {name}")
        print("Hello!!! {}".format(name))
