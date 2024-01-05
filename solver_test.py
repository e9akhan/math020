import solver


def is_solved():
    assert solver.solver(10)


def test_solver():
    assert solver.solver(10) == 3628800
