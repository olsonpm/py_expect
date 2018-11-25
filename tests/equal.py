from another_expect import expect
from .Results import Results


def runTests():
    r = Results("equal")

    a1 = {"one": 1}
    a2 = {"one": 1}
    b = {"one": "1"}
    c1 = {"two": 2, "a": a1}
    c2 = {"two": 2, "a": a2}
    d = {"two": 2, "a": b}

    try:
        expect(c1).to.equal(c2)
    except:
        r.shouldHavePassed("expect(c1).to.equal(c2)")

    try:
        expect(c1).to.equal(d)
        r.shouldHaveFailed("expect(c1).to.equal(c2)")
    except:
        pass

    return r
