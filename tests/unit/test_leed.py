import os
import sys

SOURCE_PATH = os.path.join(os.path.dirname(__file__), '../../src')
sys.path.append(SOURCE_PATH)

class switch_dir:
    def __init__(self, d):
        self.d = d
    def __enter__(self):
        self.owd = os.getcwd()
        os.chdir(self.d)
        return self
    def __exit__(self, ex_type, ex_value, tb):
        os.chdir(self.owd)
        return ex_type is None

def test_parameters():
    import tomli
    from LEED.parameter import SolverInfo

    input_data = """
    [solver]
    [solver.config]
    path_to_solver = "satl2.exe"
    [solver.reference]
    path_to_base_dir = "base"
    """

    params = tomli.loads(input_data)
    info = SolverInfo(**params["solver"])

    assert info.config.path_to_solver == "satl2.exe"
    assert info.reference.path_to_base_dir == "base"
    assert info.name == "leed"

    
def test_write_input_file():
    import odatse
    from LEED.input import Input
    import shutil
    from tempfile import TemporaryDirectory

    test_dir = os.path.dirname(__file__)

    info = odatse.Info({'base':{}, 'algorithm': {}, 'solver': {}})
    input = Input(info)

    xval = [0.1, 0.230]
    
    with TemporaryDirectory() as work_dir:
        with switch_dir(work_dir):
            shutil.copy(os.path.join(test_dir, "tleed4.i_template"), "tleed4.i")

            input._write_fit_file(xval)

            with open("tleed4.i", "r") as f:
                data_new = f.readlines()
            with open(os.path.join(test_dir, "tleed4.i_ref"), "r") as f:
                data_ref = f.readlines()

            for i, (a, b) in enumerate(zip(data_ref, data_new)):
                assert a == b, "line {} differs".format(i)
            

def test_get_results():
    import odatse
    from LEED.leed import Solver
    import shutil
    from tempfile import TemporaryDirectory
    import tomli
    import numpy as np

    test_dir = os.path.dirname(__file__)

    with open(os.path.join(test_dir, "input.toml"), "rb") as f:
        params = tomli.load(f)

    ref_value = 0.1895

    with TemporaryDirectory() as work_dir:
        with switch_dir(work_dir):
            shutil.copy(os.path.join(test_dir, "dummy.exe"), "dummy.exe")
            shutil.copytree(os.path.join(test_dir, "base_dir"), "base_dir")

            info = odatse.Info(params)
            solver = Solver(info)

            os.makedirs("output/0")
            shutil.copy(os.path.join(test_dir, "search.s"), "output/0/search.s")
            
            v = solver.get_results()
            assert np.isclose(v, ref_value), "reference value = {}".format(ref_value)
    
