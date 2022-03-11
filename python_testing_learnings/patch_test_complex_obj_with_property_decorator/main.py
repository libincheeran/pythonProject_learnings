from python_testing_learnings.patch_test_complex_obj_with_property_decorator.outer import OuterOne


def my_main_call():
    outer = OuterOne()
    inner = outer.get_inner
    val = inner.get_val
    # print(val)
    return val

# my_main_call()
