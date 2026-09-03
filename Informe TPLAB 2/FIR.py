#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 13:16:16 2026

@author: mariano
"""

import sympy as sp
import numpy as np
import scipy.signal as sig
from scipy.signal.windows import hamming, kaiser, blackmanharris
import matplotlib.pyplot as plt

from pytc2.sistemas_lineales import plot_plantilla, group_delay


# frecuencia de muestreo normalizada
fs = 2.0
# tamaño de la respuesta al impulso
cant_coef = 27

filter_type = 'lowpass'

fpass = 0.25 # 
ripple = 0.5 # dB
fstop = 0.6 # Hz
attenuation = 40 # dB

# construyo la plantilla de requerimientos
frecs = [0.0,  fpass,     fstop,          1.0]
gains = [0,   -ripple, -attenuation,   -np.inf] # dB

gains = 10**(np.array(gains)/20)

# algunas ventanas para evaluar
#win_name = 'boxcar'
#win_name = 'hamming'
#win_name = kaiser
#win_name = 'flattop'

# FIR design
num_bh = sig.firwin2(cant_coef, frecs, gains , window='blackmanharris' )
num_hm = sig.firwin2(cant_coef, frecs, gains , window='hamming' )
num_ka = sig.firwin2(cant_coef, frecs, gains , window=('kaiser',14))
den = 1.0


def plot_freq_resp_fir(this_num, this_desc):

    wrad, hh = sig.freqz(this_num, 1.0)
    ww = wrad / np.pi
    
    plt.figure(1)

    plt.plot(ww, 20 * np.log10(abs(hh)), label=this_desc)

    plt.title('FIR diseñado por métodos directos - Taps:' + str(cant_coef) )
    plt.xlabel('Frequencia normalizada')
    plt.ylabel('Modulo [dB]')
    plt.grid(which='both', axis='both')

    axes_hdl = plt.gca()
    axes_hdl.legend()
    
    plt.figure(2)

    phase = np.unwrap(np.angle(hh))

    plt.plot(ww, phase, label=this_desc)

    plt.title('FIR diseñado por métodos directos - Taps:' + str(cant_coef))
    plt.xlabel('Frequencia normalizada')
    plt.ylabel('Fase [rad]')
    plt.grid(which='both', axis='both')

    axes_hdl = plt.gca()
    axes_hdl.legend()

    plt.figure(3)

    # ojo al escalar Omega y luego calcular la derivada.
    gd_win = group_delay(wrad, phase)

    plt.plot(ww, gd_win, label=this_desc)

    plt.ylim((np.min(gd_win[2:-2])-1, np.max(gd_win[2:-2])+1))
    plt.title('FIR diseñado por métodos directos - Taps:' + str(cant_coef))
    plt.xlabel('Frequencia normalizada')
    plt.ylabel('Retardo [# muestras]')
    plt.grid(which='both', axis='both')

    axes_hdl = plt.gca()
    axes_hdl.legend()    

plot_freq_resp_fir(num_bh, filter_type+ '-blackmanharris')    
plot_freq_resp_fir(num_hm, filter_type+ '-hamming')    
plot_freq_resp_fir(num_ka, filter_type+ '-kaiser-b14')    
    
    
# sobreimprimimos la plantilla del filtro requerido para mejorar la visualización    
fig = plt.figure(1)    
plot_plantilla(filter_type = filter_type , fpass = fpass, ripple = ripple , fstop = fstop, attenuation = attenuation, fs = fs)
ax = plt.gca()
ax.legend()

# reordenamos las figuras en el orden habitual: módulo-fase-retardo
plt.figure(2)    
axes_hdl = plt.gca()
axes_hdl.legend()

plt.figure(3)    
axes_hdl = plt.gca()
axes_hdl.legend()

plt.show()

# probaremos ahora diseñar una respuesta arbitraria
frecs = [0.0,        0.2,     0.3,     0.4,      0.5,    0.6,   1.0 ]
gains = [-np.inf,   -30,      -15,   -ripple,   -ripple, -50,  -np.inf] # dB

gains = 10**(np.array(gains)/20)
    
# podemos usar los ceros estructurales de los FIR tipo 3-4 para forzar
# sendos ceros en DC-Nyquist. Recordar que necesitamos cantidad par
# de coeffs y antisimetría de la respuesta al impulso.
cant_coef = 101
fs = 2.0

# FIR re-design
num_bh = sig.firwin2(cant_coef, frecs, gains , window='blackmanharris', antisymmetric=True )
num_hm = sig.firwin2(cant_coef, frecs, gains , window='hamming', antisymmetric=True )
num_ka = sig.firwin2(cant_coef, frecs, gains , window=('kaiser',14), antisymmetric=True)

# visualizamos respuesta
plot_freq_resp_fir(num_bh, filter_type+ '-blackmanharris')    
plot_freq_resp_fir(num_hm, filter_type+ '-hamming')    
plot_freq_resp_fir(num_ka, filter_type+ '-kaiser-b14')    
    
    
# sobreimprimimos la plantilla del filtro requerido para mejorar la visualización    
plt.figure(1)    
plt.plot(frecs, 20*np.log10(gains+1e-4), 'rx', label='plantilla arbitraria' )
axes_hdl = plt.gca()
axes_hdl.legend()
axes_hdl.set_ylim(bottom=-90, top=5)

# reordenamos las figuras en el orden habitual: módulo-fase-retardo
plt.figure(2)    
axes_hdl = plt.gca()
axes_hdl.legend()

plt.figure(3)    
axes_hdl = plt.gca()
axes_hdl.legend()

plt.show()

# Imprimir los 101 coeficientes del último filtro diseñado (Kaiser)
print("Coeficientes del filtro (Kaiser):")
# np.set_printoptions(threshold=np.inf) # Descomenta esto si Python oculta los valores del medio
#print(num_ka)

# Si quieres los del filtro Hamming o Blackman-Harris:
print(num_hm)
# print(num_bh)