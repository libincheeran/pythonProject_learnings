from python_testing_learnings.patch_test_complex_obj.outer import Outer


def my_main_call():
    outer = Outer()
    inner = outer.get_inner()
    val = inner.get_val()
    print(val)
    return val

# my_main_call()
