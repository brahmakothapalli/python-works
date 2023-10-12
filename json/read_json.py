import pathlib

def get_test_data():

    ROOT_DIR = pathlib.Path(__file__).parent.parent
    print("Parent directory of the file - ", ROOT_DIR)

    print(f"appended file path is {ROOT_DIR}/json/test.json")

    print("Current file path - ",pathlib.Path(__file__))

    print("Home dir -", pathlib.Path.home())

    print("Current ",pathlib.Path.cwd())


get_test_data()