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
    [solver.reference]
    path_to_base_dir = "base"
    [solver.param]
    string_list = ["opt000", "opt001"]
    """

    params = tomli.loads(input_data)
    info = SolverInfo(**params["solver"])

    assert info.config.path_to_first_solver == "satl1.exe"
    assert info.config.path_to_second_solver == "satl2.exe"
    assert info.reference.path_to_base_dir == "base"
    assert info.name == "leed"
