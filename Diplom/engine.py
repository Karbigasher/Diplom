import pandas as pd
import numpy as np


def engine(torque, rotationFrequency):
    ddd = pd.read_json("engine_json.json")
    #ddd.to_csv('out.csv')
    # print(len(ddd))
    # print(ddd)

    
    #step_gearRatio = 4.5
    eff_zp = 0.9
    eff_podsh = 0.93
    eff = 0.6
    
    power_calc = torque*rotationFrequency/(9950*eff)
    
    try:
        new = ddd.loc[ddd['nominal_Torque'] >= power_calc].iloc[0]
    except IndexError:
        print('нет подходящего двигателя')
        return 0
    print(new)
    
    general_gearRatio = np.around(new['nominal_rotationFrequency']/rotationFrequency, 0)
    torque_calc = torque/(general_gearRatio*eff)
    
    print(general_gearRatio, torque_calc)
    
    steps = np.around(np.log(general_gearRatio)/np.log(4.5),0) 
    print(steps)
    eff = np.power(eff_zp,steps)*np.power(eff_podsh,2*steps+2)
    torque_calc = torque/(general_gearRatio*eff)
    # print(steps)
    # print(eff)
    try:
        new = ddd.loc[ddd['nominal_Torque'] >= torque_calc].iloc[0]
    except IndexError:
        print('нет подходящего двигателя')
        return 0
    print(general_gearRatio, torque_calc, eff)
    print(new)
    return new, general_gearRatio, steps

if __name__ == "__main__":
    torque = 200
    rotationFrequency = 50
    engine(torque, rotationFrequency)