from unittest.mock import Mock, patch, PropertyMock

from python_testing_learnings.test_patch_decorators import MyClass

mock = Mock()
mock.return_value = "hello"
print(mock())

# mock return value on constructor
mock = Mock(return_value="hello")
print(mock())


# side effect with callable

class Response:
    def __init__(self, code):
        self.code = code


def get_response(*args, **kwargs):
    return Response(200)


mock = Mock()
mock.side_effect = get_response
response = mock()
print(response.code)

# side effect with callable lambda

sum = lambda v1, v2: v1 + v2
mock = Mock(side_effect=sum)
print(mock(1, 1))  # prints 2
print(mock(-1, 1))  # prints 0


# Propertymocks demo for @property types

class Foo:
    @property
    def foo(self):
        return 'something'


with patch('__main__.Foo.foo', new_callable=PropertyMock) as mock_foo:
    mock_foo.return_value = 'mockity-mock'
    this_foo = Foo()
    print(this_foo.foo)

# note the below does not work
with patch('__main__.Foo', new_callable=PropertyMock) as mock_foo:
    mock_foo.foo.return_value = 'mockity-mock'
    this_foo = Foo()
    print(this_foo.foo)



# check if you are mocking the right class
class SomeClass:
    def __init__(self):
        pass

@patch('__main__.SomeClass')
def function(normal_argument, mock_class):
    print(mock_class is SomeClass)

function(None)



#mocking method when only patching the class
class Class:
    def method(self):
        pass


with patch('__main__.Class') as MockClass:
    instance = MockClass.return_value
    instance.method.return_value = 'foo'
    assert Class() is instance
    assert Class().method() == 'foo'

