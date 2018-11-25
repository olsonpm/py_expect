from ...test import test
from .be import be
from .mixinRaise_ import mixinRaise_


class to(mixinRaise_):
    def __init__(self, expectInst):
        self._expectInst = expectInst
        self._actual = self._expectInst._actual
        self.be = be(expectInst)

    @test
    def equal(self, expected):
        actual = self._actual

        if actual == expected:
            return

        return f"expected {actual} to equal {expected}"

    @test
    def haveType(self, expected):
        expectInst = self._expectInst

        actualType = type(expectInst._actual)
        if actualType is expected:
            return

        actualName = actualType.__name__
        expectedName = expected.__name__
        return f"expected type '{expectedName}' but got '{actualName}'"
