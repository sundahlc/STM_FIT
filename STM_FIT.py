import streamlit as st
import pandas as pd
import numpy as np
from scipy import optimize
from matplotlib import pyplot as pl

def dynes(E, gamma, delta, N0):
    numerator = E - gamma*1j
    denominator = np.sqrt( (E-gamma*1j)**2 - delta**2 )
    return N0*np.abs(np.real(numerator/denominator))

f = 'stm.csv'
stm = pd.read_csv(f, names=['bias', 'didv'])
# try:
#     f = 'C:/Users/Kuri y Rizu/Documents/Synced Folders/UW-Madison/Oxide Lab/UW Papers/RF Q0 paper/stm.csv'
#     stm = pd.read_csv(f, names=['bias', 'didv'])
# except:
#     f = '/home/chris/Documents/Synced Folders/UW-Madison/Oxide Lab/UW Papers/RF Q0 paper/stm.csv'
#     stm = pd.read_csv(f, names=['bias', 'didv'])

p, cov = optimize.curve_fit(dynes, stm.bias, stm.didv, p0=[0.2, 3, 1])

gamma = st.slider('gamma', min_value=0.0, max_value=1.0, step=0.01, value=float(p[0]))
delta = st.slider('delta', min_value=0.0, max_value=4.0, step=0.1, value=float(p[1]))
N0 = st.slider('N0', min_value=0.0, max_value=1.2, step=0.01, value=float(p[2]))

fit = dynes(stm['bias'], gamma, delta, N0)

fig = pl.figure()
pl.plot(stm['bias'], stm['didv'], '-o', color='blue')
pl.plot(stm['bias'], fit, '-', color='red')

st.pyplot(fig)