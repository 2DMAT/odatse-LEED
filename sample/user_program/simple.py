# Import required modules from odatse package
import odatse
import odatse.algorithm.min_search
from odatse.extra.LEED import Solver

# Load configuration from input.toml file
# The file contains parameters like dimension, solver settings, and algorithm parameters
info = odatse.Info.from_file("input.toml")

# Initialize LEED solver with configuration
# This solver performs Low Energy Electron Diffraction calculations
solver = Solver(info)

# Create a runner that manages execution of the solver
runner = odatse.Runner(solver, info)

# Initialize minimum search algorithm with configuration and runner
# This performs optimization to find parameters that best match experimental data
alg = odatse.algorithm.min_search.Algorithm(info, runner)

# Execute the main optimization loop
alg.main()
