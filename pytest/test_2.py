#  当需要编写多个测试样例的时候，我们可以将其放到一个测试类当中，如：

class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')