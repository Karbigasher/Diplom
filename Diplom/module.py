import numpy as np
import pandas as pd


def module(d_engine, M):

    modules = pd.read_fwf("possible_modules.txt")
    z = 20
    module = (2*d_engine)/(z+2)

    module = modules.loc[modules['module'] >= module].values[0][0]
    b = 5*module

    sig = (2 * 5 * M * 1.5)/(np.power(module, 2) * z * b)
    print(f'hut {module}')
    print(sig)

    return module


if __name__ == "__main__":
    d_engine = 7
    M = 44
    module(d_engine, M)
