"""
    Module name :- solver
    Method(s) :- solver()
"""


def solver(n):
    """
    Finds factorial of n.

    Args:-
        n(int) :- An integer number.

    Return
        Factorial of n.
    """
    product = "1"

    for i in range(2, n + 1):
        carry = 0
        product_reverse_copy = product[::-1]
        product = ""

        for digit in product_reverse_copy:
            prod = carry + int(digit) * i
            product = str(prod % 10) + product
            carry = prod // 10

        if carry:
            product = str(carry) + product

    return product


if __name__ == "__main__":
    print(f"solver(10) = {solver(10)}")
