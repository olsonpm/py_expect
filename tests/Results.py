# ------- #
# Imports #
# ------- #

from simple_chalk import green, red
from another_expect.fns import isEmpty


# ---- #
# Init #
# ---- #

x = red("✘")
o = green("✔")


# ---- #
# Main #
# ---- #


class Results:
    def __init__(self, name):
        self.name = name
        self.codeThatShouldHavePassed = []
        self.codeThatShouldHaveFailed = []

    def shouldHavePassed(self, code):
        self.codeThatShouldHavePassed.append(code)

    def shouldHaveFailed(self, code):
        self.codeThatShouldHaveFailed.append(code)

    def printResults(self):
        codeThatShouldHavePassed = self.codeThatShouldHavePassed
        codeThatShouldHaveFailed = self.codeThatShouldHaveFailed
        name = self.name

        if isEmpty(codeThatShouldHavePassed + codeThatShouldHaveFailed):
            print(f"{o} {name}")
        else:
            print()
            print(f"{name}")

            for code in codeThatShouldHavePassed:
                print(f"  {x} '{code}' should have passed")

            for code in codeThatShouldHaveFailed:
                print(f"  {x} '{code}' should have failed")

            print()
