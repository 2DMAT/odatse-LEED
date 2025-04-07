import os
import sys

SOURCE_PATH = os.path.join(os.path.dirname(__file__), '../../src')
sys.path.append(SOURCE_PATH)

import numpy as np
from tempfile import NamedTemporaryFile

from LEED.rfactor import RFactor

def gen_conf():
    rng = np.random.default_rng(1)
    ee = np.linspace(100.0, 200.0, 101)
    th = 1.0 / ((ee-130)**2 + 5**2) + 1.2 / ((ee-160)**2 + 10**2)
    ex = 0.04 * np.exp(-(ee-130.0)**2 / (2 * 5.0**2)) + 0.012 * np.exp(-(ee-160.0)**2 / (2 * 10.0**2))
    # ex += rng.normal(scale=1e-3, size=len(ee))
    return ee, ex, th

def test_param_mode_str():
    rf = RFactor(modes="rpe")
    assert True

def test_param_mode_dict():
    rf = RFactor(modes={"rpe":1.0})
    assert True

def test_param_mode_list():
    import pytest
    with pytest.raises(ValueError) as e:
        rf = RFactor(modes=["rpe"])
    assert str(e.value).startswith("unsupported mode type")

def test_param_mode_none():
    import pytest
    with pytest.raises(ValueError) as e:
        rf = RFactor(modes=None)
    assert str(e.value).startswith("unsupported mode type")

def test_mode_skip():
    rf = RFactor(modes="vue")
    rf.modes= []  # this may not happen
    r = rf.evaluate(*gen_conf())
    assert r == float("inf")

def test_mode_unknown():
    import pytest
    with pytest.raises(ValueError) as e:
        rf = RFactor(modes="vue")
        r = rf.evaluate(*gen_conf())
    assert str(e.value) == "unknown mode \"vue\""

def test_mode_r1():
    rf = RFactor(modes="r1", rescale=True)
    r = rf.evaluate(*gen_conf())
    assert np.isclose(r, 0.24326499637406562)

def test_mode_r2():
    rf = RFactor(modes="r2", rescale=True)
    r = rf.evaluate(*gen_conf())
    assert np.isclose(r, 0.0378279351680381)

def test_mode_r2_norescale():
    rf = RFactor(modes="r2", rescale=False)
    r = rf.evaluate(*gen_conf())
    assert np.isclose(r, 0.02570190979362669)

def test_mode_rp1():
    rf = RFactor(modes="rp1", rescale=True)
    r = rf.evaluate(*gen_conf())
    assert np.isclose(r, 0.39187839233005234)

def test_mode_rp2():
    rf = RFactor(modes="rp2", rescale=True)
    r = rf.evaluate(*gen_conf())
    assert np.isclose(r, 0.13550933662673503)

def test_mode_rpp1():
    rf = RFactor(modes="rpp1", rescale=True)
    r = rf.evaluate(*gen_conf())
    assert np.isclose(r, 0.7288895359917832)

def test_mode_rpp2():
    rf = RFactor(modes="rpp2", rescale=True)
    r = rf.evaluate(*gen_conf())
    assert np.isclose(r, 0.5610483649686006)

def test_mode_rrzj():
    rf = RFactor(modes="rrzj", rescale=True)
    r = rf.evaluate(*gen_conf())
    assert np.isclose(r, 0.06772955465329485)

def test_mode_rmzj():
    rf = RFactor(modes="rmzj", rescale=True)
    r = rf.evaluate(*gen_conf())
    assert np.isclose(r, 0.06844756382980467)

def test_mode_rpe():
    rf = RFactor(modes="rpe", vi=-5.0, persh=0.1, rescale=True)
    r = rf.evaluate(*gen_conf())
    assert np.isclose(r, 0.07817608484645547)

def test_mode_rpe_norescale():
    rf = RFactor(modes="rpe", vi=-5.0, persh=0.1, rescale=False)
    r = rf.evaluate(*gen_conf())
    assert np.isclose(r, 0.07817608484645547)

def test_mode_rpe_no_vi():
    import pytest
    with pytest.raises(AssertionError) as e:
        rf = RFactor(modes="rpe", vi=None, rescale=True)
        r = rf.evaluate(*gen_conf())
    assert str(e.value) == "vi not set"

def test_mode_mix():
    rf = RFactor(modes={"r1": 1, "r2": 2}, rescale=True)
    r = rf.evaluate(*gen_conf())
    assert np.isclose(r, (0.24326499637406562 + 2 * 0.0378279351680381) / 3)

def test_deriv_smooth():
    rf = RFactor(modes="r2", smoothing_factor=1.0, rescale=True)
    r = rf.evaluate(*gen_conf())
    assert np.isclose(r, 0.041105798564902415)

def test_output():
    rf = RFactor(modes="r2", vi=0.0, rescale=True)
    with NamedTemporaryFile(delete=True) as t:
        print(t.name)
        rf._calc(["rpe"], *gen_conf(), output=t.name)
    assert True
