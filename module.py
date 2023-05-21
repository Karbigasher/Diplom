import numpy as np
import pandas as pd

def main():

    modules = pd.read_fwf("possible_modules.txt")
    d_engine = 7
    M = 44
    z = 20
    module = d_engine/11
    

    module = modules.loc[modules['module'] >= module].values[0][0]
    b = 5*module

    sig = (2 * 5 * M * 1.5)/(np.power(module,2) * z * b)
    print(f'hut {module}')
    print(sig)
    




if __name__=="__main__":
    main()