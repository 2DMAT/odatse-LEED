import py2dmat
import py2dmat.algorithm.min_search
from odatse.extra.leed import Solver

info = py2dmat.Info.from_file("input.toml")

solver = Solver(info)
runner = py2dmat.Runner(solver, info)
alg = py2dmat.algorithm.min_search.Algorithm(info, runner)
alg.main()
