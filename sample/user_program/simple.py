import odatse
import odatse.algorithm.min_search
from odatse.extra.LEED import Solver

info = odatse.Info.from_file("input.toml")

solver = Solver(info)
runner = odatse.Runner(solver, info)
alg = odatse.algorithm.min_search.Algorithm(info, runner)
alg.main()
