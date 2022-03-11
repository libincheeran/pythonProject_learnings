# Mock the complex outer and provide the simple inner class
from unittest.mock import patch, PropertyMock

import pytest

from python_testing_learnings.patch_test_complex_obj_with_property_decorator.inner import InnerOne
from python_testing_learnings.patch_test_complex_obj_with_property_decorator.main import my_main_call
from python_testing_learnings.patch_test_complex_obj_with_property_decorator.outer import OuterOne


# def get_inner(hello):
#     return InnerOne("hello")
#
#
# def get_val(hello):
#     return "mock"
#
#
# def test_main(monkeypatch):
#     monkeypatch.setattr("python_testing_learnings.patch_test_complex_obj_with_property_decorator.inner.InnerOne.get_val", get_val)
#     monkeypatch.setattr("python_testing_learnings.patch_test_complex_obj_with_property_decorator.outer.OuterOne.get_inner", get_inner)
#     val = my_main_call()
#     print(val)

# this is working
# @patch.object(OuterOne,"get_inner", new_callable=PropertyMock)
# def test_main(mocked_inner):
#     mocked_inner.return_value = InnerOne("mock")
#     val = my_main_call()
#     print(val)

# @pytest.fixture
# @patch.object(OuterOne, "get_inner", new_callable=PropertyMock)
# @patch.object(OuterOne)
# def get_outer_one(mocked_outer, mocked_inner):
#     mocked_inner.return_value = InnerOne("mock")
#     val = my_main_call()
#     print(val)


@patch("python_testing_learnings.patch_test_complex_obj_with_property_decorator.main.OuterOne")
def test_main(mocked_outer):
    outer_instance = mocked_outer.return_value
    outer_instance.get_inner = InnerOne("mock")
    val = my_main_call()
    print(val)
