from another_expect import expect
from .Results import Results


class Person:
    pass


class Batman(Person):
    pass


me = Person()
bruce = Batman()


def runTests():
    r = Results("anInstanceOf")

    try:
        expect(bruce).to.be.anInstanceOf(Person)
    except:
        r.shouldHavePassed("expect(bruce).to.be.anInstanceOf(Person)")

    try:
        expect(me).to.haveType(Batman)
        r.shouldHaveFailed("expect(me).to.be.anInstanceOf(Batman)")
    except:
        pass

    return r
