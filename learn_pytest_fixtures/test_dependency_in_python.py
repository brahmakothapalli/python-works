import pytest


class TestDependencyMethods:

    @pytest.mark.dependency()
    def test_method_login(self):
        print("login app")

    @pytest.mark.dependency(depends=["TestDependencyMethods::test_method_login"])
    def test_method_add_to_cart(self):
        print("add product to the cart")

    @pytest.mark.dependency(depends=["TestDependencyMethods::test_method_add_to_cart"])
    def test_method_checkout(self):
        print("checkout the product")
        assert False

    @pytest.mark.dependency(depends=["TestDependencyMethods::test_method_checkout"])
    def test_method_logout(self):
        print("logout app")
