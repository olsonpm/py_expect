from . import anInstanceOf, be, equal, haveType, raise_

modules = [anInstanceOf, be, equal, haveType, raise_]


def runTests():
    for m in modules:
        results = m.runTests()
        results.printResults()


__all__ = ["runTests"]
