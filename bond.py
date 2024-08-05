'''
Bond Pricing with
Cox-Ingersoll-Ross (CIR) Interest Rate Model
'''

import numpy as np
import pandas as pd
import ctypes

cd = ctypes.c_double
ci = ctypes.c_int

gs = ctypes.CDLL("./bond.so")
gs.InterestRate.argtypes = (cd, cd, cd, cd, cd, ci, ci)
gs.InterestRate.restype = cd

def Calibrate(x, dt):
    mu = np.mean(x)
    s2 = np.std(x)**2
    y1 = (1.0/(len(x) - 1))*np.sum([(x[i] - mu)*(x[i-1] - mu) for i in range(1, len(x))])

    alpha = -np.log(y1/s2)/dt
    sigma = np.sqrt(2.0*alpha*s2/mu)

    return alpha, mu, sigma

rates = pd.read_csv('rates.csv')[::-1]

R = (rates['1 Yr'].values/100.0).tolist()

par_value = 1000
coupon_rate = 0.036
periods = 2
maturity = 5

T = maturity*periods
CF = par_value*coupon_rate/periods

N = 400
Paths = 20

dt = T / N

alpha, mu, sigma = Calibrate(R, dt)

R0 = R[-1]

bond_price = 0

for t in range(T):
    R0 = gs.InterestRate(alpha, mu, sigma, R0, dt, N, Paths)
    discount_rate = R0/periods
    bond_price += CF/pow(1 + discount_rate, t + 1)

bond_price += par_value/pow(1 + discount_rate, T)

print('Bond Price: ', bond_price)

