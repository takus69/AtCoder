from A import Solver


if __name__ == '__main__':
    solver = Solver()
    solver.set_filepath('testcases/sample')
    solver.read_input()
    solver.make_plan()
    solver.submission()
    solver.evaluate()
