import pandas as pd
import numpy as np


def main():
    ddd = pd.read_json("SL-engines.json")
    #ddd.to_csv('out.csv')
    print(len(ddd))
    print(ddd)

    torque = 200
    general_gearRatio = 50
    step_gearRatio = 4.5
    eff_zp = 0.9
    eff_podsh = 0.93
    eff = 0.6


    torque_calc = torque/(general_gearRatio*eff)
    steps = np.around(np.log(general_gearRatio)/np.log(step_gearRatio),0)

    eff = np.power(eff_zp,steps)*np.power(eff_podsh,2*steps+2)
    torque_calc = torque/(general_gearRatio*eff)
    print(steps)
    print(eff)
    try:
        new = ddd.loc[ddd['nominal_Torque'] >= torque_calc].iloc[0]
    except IndexError:
        print('нет подходящего двигателя')
        return 0

    
    print(new)

if __name__ == "__main__":
    main()
