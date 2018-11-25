from another_expect import expect
from .Results import Results


class MyErr(Exception):
    pass


class NotMyErr(Exception):
    pass


def raiseMyErr():
    raise MyErr("this partial string exists")


def runTests():
    r = Results("raise_")

    try:
        expect(raiseMyErr).to.raise_(MyErr)
    except:
        r.shouldHavePassed("expect(raiseMyErr).to.raise_(MyErr)")

    try:
        expect(raiseMyErr).to.raise_("partial string")
    except:
        r.shouldHavePassed('expect(raiseMyErr).to.raise_("partial string")')

    try:
        expect(raiseMyErr).to.raise_(NotMyErr)
        r.shouldHaveFailed("expect(raiseMyErr).to.raise_(NotMyErr)")
    except:
        pass

    try:
        expect(raiseMyErr).to.raise_("full string")
        r.shouldHaveFailed('expect(raiseMyErr).to.raise_("full string")')
    except:
        pass

    return r
