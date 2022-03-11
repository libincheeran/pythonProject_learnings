
# Mock the complex outer and provide the simple inner class
from unittest.mock import patch, PropertyMock

from python_testing_learnings.patch_test_complex_obj.inner import Inner
from python_testing_learnings.patch_test_complex_obj.main import my_main_call


@patch("python_testing_learnings.patch_test_complex_obj.main.Outer")
def test_main(mock_outer):
    inner = Inner("mock")
    mock_outer.return_value.get_inner.return_value = inner
    val = my_main_call();
    print(val)


# # @patch("python_testing_learnings.patch_test_complex_obj.main.Outer.Inner", new_callable=PropertyMock)
# @patch("python_testing_learnings.patch_test_complex_obj.main.Outer", new_callable=PropertyMock)
# def test_main(mock_outer, mock_inner):
#     inner = Inner("mock")
#     # mock_outer.return_value.get_inner.return_value = inner
#     val = my_main_call();
#     print(val)