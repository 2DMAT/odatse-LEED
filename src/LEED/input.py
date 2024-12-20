# odatse-LEED -- Low Energy Electron Diffraction solver module for ODAT-SE
# Copyright (C) 2024- The University of Tokyo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see http://www.gnu.org/licenses/.

from typing import Dict, List, Tuple
from pathlib import Path

import os.path
import numpy as np

class Input(object):
    root_dir: Path
    output_dir: Path
    dimension: int

    def __init__(self, info):
        """
        Initialize the Input class with the given information.

        Parameters
        ----------
        info : odatse.Info
            An object containing base information.
        """
        self.dimension = info.solver.get("dimension", None) or info.base.get("dimension", None)
        self.root_dir = info.base["root_dir"]
        self.output_dir = info.base["output_dir"]

    def prepare(self, x: np.ndarray, args):
        """
        Prepare the input by deleting output files and generating a fit file.

        Parameters
        ----------
        x : np.ndarray
            A numpy array of variables.
        args : tuple
            Additional arguments.
        """
        x_list = x
        #step, iset = args
        #extra = iset > 0

        # Delete output files
        delete_files = ["search.s", "gleed.o"]
        for file in delete_files:
            if os.path.exists(file):
                os.remove(file)
        # Generate fit file
        # Add variables by numpy array.(Variables are updated in optimization process).
        self._write_fit_file(x_list)

    def _write_fit_file(self, variables):
        """
        Write the fit file with the given variables.

        Parameters
        ----------
        variables : np.ndarray
            A numpy array of variables to be written into the fit file.
        """
        file_name = "tleed4.i"
        with open(file_name, "r") as fr:
            contents = fr.read()
        for idx, variable in enumerate(variables):
            # FORTRAN format: F7.6
            str_variable = str(variable).zfill(6)[:6]
            contents = contents.replace(
                "opt{}".format(str(idx).zfill(3)), str_variable
            )
        with open(file_name, "w") as writer:
            writer.write(contents)
