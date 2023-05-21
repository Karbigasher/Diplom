import numpy as np
from scipy.optimize import minimize, NonlinearConstraint, LinearConstraint, Bounds


def Optim(steps_gearRatio, *args):
    steps = len(steps_gearRatio)
    bistr = np.copy(steps_gearRatio)
    bistr = 1/bistr
    for it in range(1, steps):
        bistr[it] = bistr[it]*bistr[it-1]
    bistr = bistr**2
    bistr = bistr*(np.copy(steps_gearRatio)**4)
    return np.sum(bistr)


def arg_constr(x):
    return np.prod(x) - general_gearRatio


general_gearRatio = 210
z = 20
m = 0.5
initial_guess=[3, 3.5, 4, 5]
constraints = [NonlinearConstraint(Optim, 0, np.inf), {
    'type': 'eq', 'fun': arg_constr}]
bonds = Bounds(lb=3, ub=6)

print(Optim(np.array([3, 3.5, 4, 5])))
resh = minimize(Optim, initial_guess, args=(z,m), method='SLSQP',
                constraints=constraints, bounds=bonds)
print(resh.x, resh.fun)
