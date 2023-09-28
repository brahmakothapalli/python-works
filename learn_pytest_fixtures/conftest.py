import pytest


@pytest.fixture(scope='session', autouse=True)
def before_suite(request):
    print("this will be executed before the suite or all the test classes")
    print("like db connection established")

    def close_db():
        print("closing db config")
    request.addfinalizer(close_db)
