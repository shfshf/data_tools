class TestClassOne(object):
    def test_one(self):
        x = "this"
        assert 't'in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')


class TestClassTwo(object):
    def test_one(self):
        x = "iphone"
        assert 'p'in x

    def test_two(self):
        x = "apple"
        print("fuck")
        assert hasattr(x, 'check')