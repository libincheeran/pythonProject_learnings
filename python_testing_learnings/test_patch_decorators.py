from unittest.mock import patch


class MyClass:
    def method(self):
        pass


# using patch decorators
@patch("python_testing_learnings.test_patch_decorators.MyClass")
def test_class(mock_class):
    assert MyClass() is mock_class.return_value
    mock_class.return_value.method.return_value = "foo"
    assert MyClass().method() == "foo"



# another example
class SomeClass:
    def class_method(self, val):
        pass

    def static_method(self, val):
        pass


@patch.object(SomeClass, 'class_method')
def test(mock_method):
    SomeClass.class_method(3)
    mock_method.assert_called_with(3)


#Nesting patching decorators

@patch.object(SomeClass, 'class_method')
@patch.object(SomeClass, 'static_method')
def test(mock1, mock2):
    assert SomeClass.static_method is mock1
    assert SomeClass.class_method is mock2
    SomeClass.static_method('foo')
    SomeClass.class_method('bar')
    mock1.assert_called_once_with('foo')
    mock2.assert_called_once_with('bar')
