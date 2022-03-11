from python_testing_learnings.patch_test_complex_obj.inner import Inner


class Outer:
    def __init__(self, name=None):
        print("called outer init")

    def get_inner(self):
        return Inner("hello")
