from ortools.sat.python import cp_model
from ortools.linear_solver import pywraplp


def master_spark_solver(test_cases):
    for X, Y, n, sparks in test_cases:
        model = cp_model.CpModel()
        x = model.NewIntVar(0, X, 'x')
        y = model.NewIntVar(0, Y, 'y')
        model.Add(x > 0)
        model.Add(y > 0)
        model.Add(x < X)
        model.Add(y < Y)

        for Ai, Bi, Ci, Di in sparks:
            not_in_spark = model.NewBoolVar('not_in_spark')
            model.Add(Ai * x + Bi * y <= Ci).OnlyEnforceIf(not_in_spark)
            model.Add(Ai * x + Bi * y >= Di).OnlyEnforceIf(not_in_spark.Not())

        solver = cp_model.CpSolver()
        status = solver.Solve(model)

        if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
            return 1
    return 0


def testcase_input(precision: int):
    X, Y, n = map(int, input().split())
    sparks = []
    for i in range(n):
        ai, bi, ci, di = map(int, input().split())
        sparks.append((ai, bi, ci * precision, di * precision))
    return X * precision, Y * precision, n, sparks


if __name__ == '__main__':
    T = int(input())
    output = []
    for i in range(T):
        X, Y, n, sparks = testcase_input(precision=100)
        testcase = [(X, Y, n, sparks)]
        output.append(master_spark_solver(testcase))

    print(*output, sep="")
