import numpy as np
from scipy.optimize import minimize, NonlinearConstraint, Bounds


def Optim(steps_gearRatio, *args):
    steps = len(steps_gearRatio)
    bistr = np.copy(steps_gearRatio)
    bistr = 1/bistr
    for it in range(1, steps):
        bistr[it] = bistr[it]*bistr[it-1]
    bistr = bistr**2
    bistr = bistr*(np.copy(steps_gearRatio)**4)
    return np.sum(bistr)


def optim_bistr(general_gearRatio, m, steps):
    z = 20
    initial_guess=np.full((4),general_gearRatio/np.exp(steps))
    constraints = [NonlinearConstraint(Optim, 0, np.inf), {
        'type': 'eq', 'fun': lambda x: np.prod(x) - general_gearRatio}]
    bonds = Bounds(lb=3, ub=6)
    
    print(Optim(initial_guess))
    resh = minimize(Optim, initial_guess, args=(z,m), method='SLSQP',
                    constraints=constraints, bounds=bonds)
    print(resh.x, resh.fun)

if __name__ == "__main__":
    m = 0.5
    general_gearRatio = 210
    steps = 4
    optim_bistr(general_gearRatio, m, steps)