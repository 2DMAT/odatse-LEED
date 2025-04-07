import numpy as np
import fortranformat as ff

def gen_conf():
    rng = np.random.default_rng(1)
    ee = np.linspace(100.0, 200.0, 101)
    th = 1.0 / ((ee-130)**2 + 5**2) + 1.2 / ((ee-160)**2 + 10**2)
    ex = 0.04 * np.exp(-(ee-130.0)**2 / (2 * 5.0**2)) + 0.012 * np.exp(-(ee-160.0)**2 / (2 * 10.0**2))
    # ex += rng.normal(scale=1e-3, size=len(ee))
    return ee, ex, th

if __name__ == "__main__":
    ee, ex, th = gen_conf()

    # modified format
    format_ex = ff.FortranRecordWriter('(F8.3,\',\',E18.10)')
    format_th = ff.FortranRecordWriter('(F8.3,\',,\',E18.10)')

    print("ENERGY,EXP,THEORY,RFAC{:2d}={:6.4f},BEAM {}".format(1, 0.0, "(1,1)"))
    for i in range(len(ee)):
        print(format_ex.write([ee[i], ex[i]]))
    for i in range(len(ee)):
        print(format_th.write([ee[i], th[i]]))

    # # original format
    # fmt = ff.FortranRecordWriter('(F11.4,E19.7)')

    # print("titletext: {} beam {} rfac{:2d}={:6.4f}".format("artificial", "(1,0)", 1, 0.0))
    # print(" \"IV exp")
    # for i in range(len(ee)):
    #     print(fmt.write([ee[i], ex[i]]))
    # print()
    # print(" \"IV theory")
    # for i in range(len(ee)):
    #     print(fmt.write([ee[i], th[i]]))
    # print()
