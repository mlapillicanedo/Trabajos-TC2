# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 17:24:42 2026

@author: juanm
"""

import numpy as np
from scipy import signal as sig
import sympy as sp
from matplotlib import pyplot as plt
from pytc2.remociones import remover_polo_dc
from pytc2.general import a_equal_b_latex_s, print_latex, s, symbfunc2tf, factorSOS
from pytc2.sistemas_lineales import bodePlot, pzmap, GroupDelay, analyze_sys
from pytc2.sistemas_lineales import pretty_print_lti
from pytc2.general import print_latex, a_equal_b_latex_s
from pytc2.cuadripolos import calc_MAI_ztransf_ij_mn
from pytc2.cuadripolos import calc_MAI_vtransf_ij_mn
import sympy as sp


# Especificaciones
f0 = 50.0
BW = 1.0
fs_muestreo = 20000.0

# Factor de calidad
Q = f0 / BW

# Filtro notch
b, a = sig.iirnotch(f0, Q, fs=fs_muestreo)

# Lo paso a SOS para trabajar igual que antes
sos = sig.tf2sos(b, a)

print("SOS:")
print(sos)

# Respuesta en frecuencia
w, h = sig.sosfreqz(
    sos,
    worN=200000,
    fs=fs_muestreo
)

plt.figure(figsize=(8,5))

plt.plot(
    w,
    20*np.log10(np.maximum(np.abs(h), 1e-8))
)

plt.axvline(f0, linestyle='--', label='f notch = 50 Hz')

# Bordes de BW de 1 Hz
plt.axvline(49.5, linestyle='--')
plt.axvline(50.5, linestyle='--')

plt.axhline(-3, linestyle='--', label='-3 dB')

plt.xlim(45, 55)
plt.ylim(-80, 2)

plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud [dB]')
plt.title('Filtro Notch 50 Hz - BW = 1 Hz')

plt.grid(True)
plt.legend()
plt.show()