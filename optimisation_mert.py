import numpy as np
from scipy.optimize import minimize, NonlinearConstraint, Bounds


def Optim(steps_gearRatio, *args):
    steps = len(steps_gearRatio)
    copy = np.copy(steps_gearRatio)
    j = 8.6 * m + steps_gearRatio + 4.4
    delta_phi = 7.4 * j/(m * z * steps_gearRatio)
    for it in range(1, steps):
        copy[it] = copy[it]*copy[it-1]
    return np.sum(delta_phi*copy/general_gearRatio)

    
def arg_constr(x):
    return np.prod(x) - general_gearRatio


general_gearRatio = 210

constraints = [NonlinearConstraint(Optim, 0, np.inf), {
    'type': 'eq', 'fun': arg_constr}]
bonds = Bounds(lb=3, ub=6)
z = 20
m = 0.5
initial_guess = [3, 3.5, 4, 5]
resh = minimize(Optim, initial_guess, args=(z, m), method='SLSQP',
                constraints=constraints, bounds=bonds)
print(resh.x, resh.fun)


