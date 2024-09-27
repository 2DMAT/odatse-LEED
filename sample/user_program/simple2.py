import odatse
import odatse.algorithm.min_search
from odatse.extra.LEED import Solver

params = {
    "base": {
        "dimension": 2,
        "output_dir": "output",
    },
    "solver": {
        "config": {
            "path_to_solver": "./leedsatl/satl2.exe",
        },
        "reference": {
            "path_to_base_dir": "./base",
        },
    },
    "algorithm": {
        "label_list": ["z1", "z2"],
        "param": {
            "min_list": [-0.5, -0.5],
            "max_list": [0.5, 0.5],
            "initial_list": [-0.1, 0.1],
        },
         
    },
}

info = odatse.Info(params)

solver = Solver(info)
runner = odatse.Runner(solver, info)
alg = odatse.algorithm.min_search.Algorithm(info, runner)
alg.main()
