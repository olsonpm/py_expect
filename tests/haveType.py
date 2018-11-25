from another_expect import expect
from .Results import Results


class Person:
    pass


class Batman(Person):
    pass


bruce = Batman()


def runTests():
    r = Results("haveType")

    try:
        expect(bruce).to.haveType(Batman)
    except:
        r.shouldHavePassed("expect(bruce).to.haveType(Batman)")

    try:
        expect(bruce).to.haveType(Person)
        r.shouldHaveFailed("expect(bruce).to.haveType(Person)")
    except:
        pass

    return r
