"""
    Module name :- answer
    Method(s) :- answer()
"""

from solver import solver


def answer():
    """
    Finds factorial of n.

    Args:-
        n(int) :- An integer number.

    Return
        Factorial of n.
    """
    return solver(100)


if __name__ == "__main__":
    print(f"answer() = {answer()}")
