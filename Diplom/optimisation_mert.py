import numpy as np
from scipy.optimize import minimize, Bounds


def Optim(steps_gearRatio, *args):
    general_gearRatio = np.prod(steps_gearRatio)
    z, m = args
    steps = len(steps_gearRatio)
    copy = np.copy(steps_gearRatio)
    j = 8.6 * m + steps_gearRatio + 4.4
    delta_phi = 7.4 * j/(m * z * steps_gearRatio)
    for it in range(1, steps):
        copy[it] = copy[it]*copy[it-1]
    return np.sum(delta_phi*copy/general_gearRatio)


def optim_mert(general_gearRatio, m, steps):
    z = 20
    initial_guess = np.full((steps), general_gearRatio/np.exp(steps))

    constraints = {
        'type': 'eq', 'fun': lambda x: np.prod(x) - general_gearRatio}
    bonds = Bounds(lb=3, ub=6)

    resh = minimize(Optim, initial_guess, args=(z, m), method='SLSQP',
                    constraints=constraints, bounds=bonds)
    print(resh.x, resh.fun)

    return np.around(resh.x, 1), np.around(resh.fun, 1)


if __name__ == "__main__":
    m = 0.5
    general_gearRatio = 210
    steps = 4
    optim_mert(general_gearRatio, m, steps)
