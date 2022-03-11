from python_testing_learnings.patch_test_complex_obj_with_property_decorator.inner import InnerOne


class OuterOne:
    def __init__(self, name=None):
        print("called outer init")

    @property
    def get_inner(self):
        return InnerOne("hello")
