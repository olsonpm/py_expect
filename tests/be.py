from another_expect import expect
from .Results import Results


def runTests():
    r = Results("be")

    try:
        expect(1).to.be(1)
    except:
        r.shouldHavePassed("expect(1).to.be(1)")

    try:
        expect(1).to.be("1")
        r.shouldHaveFailed('expect(1).to.be("1")')
    except:
        pass

    return r
