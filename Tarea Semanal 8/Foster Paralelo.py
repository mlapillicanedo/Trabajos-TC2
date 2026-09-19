#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 12:52:30 2026

@author: mariano
"""

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(11, 4.5), dpi=300)
ax.set_xlim(-0.5, 9.5)
ax.set_ylim(-1.5, 4.5)
ax.axis('off')

# Terminales de entrada
ax.plot(0, 3.5, 'o', fillstyle='none', color='black', markersize=8, mew=1.5)
ax.plot(0, 0, 'o', fillstyle='none', color='black', markersize=8, mew=1.5)

# Rieles conductores superior e inferior
ax.plot([0.1, 8.5], [3.5, 3.5], 'k-', lw=1.5)
ax.plot([0.1, 8.5], [0, 0], 'k-', lw=1.5)

# Puntos suspensivos en los rieles
ax.text(5.9, 3.5, r'$\cdots$', ha='center', va='center', fontsize=18, backgroundcolor='white')
ax.text(5.9, 0, r'$\cdots$', ha='center', va='center', fontsize=18, backgroundcolor='white')

def dibujar_inductor(ax, x, y_top, y_bot, n_turns=5, r=0.18):
    dy = ((y_top - 0.2) - (y_bot + 0.2)) / n_turns
    ax.plot([x, x], [y_top, y_top - 0.2], 'k-', lw=1.5)
    ax.plot([x, x], [y_bot + 0.2, y_bot], 'k-', lw=1.5)
    for i in range(n_turns):
        center_y = (y_top - 0.2) - (i + 0.5) * dy
        theta = np.linspace(-np.pi/2, np.pi/2, 30)
        ax.plot(x + r * np.cos(theta), center_y + (dy/2) * np.sin(theta), 'k-', lw=1.5)

def dibujar_capacitor(ax, x, y_top, y_bot, plate_w=0.45, gap=0.15):
    mid_y = (y_top + y_bot) / 2
    ax.plot([x, x], [y_top, mid_y + gap/2], 'k-', lw=1.5)
    ax.plot([x, x], [mid_y - gap/2, y_bot], 'k-', lw=1.5)
    ax.plot([x - plate_w/2, x + plate_w/2], [mid_y + gap/2, mid_y + gap/2], 'k-', lw=1.5)
    ax.plot([x - plate_w/2, x + plate_w/2], [mid_y - gap/2, mid_y - gap/2], 'k-', lw=1.5)

# Rama 1: L0
dibujar_inductor(ax, 1.5, 3.5, 0, n_turns=6, r=0.22)
ax.text(1.2, 2.5, r'$L_0 = \frac{1}{k_0}$', ha='right', va='center', fontsize=15)

# Rama 2: C_inf
dibujar_capacitor(ax, 3.2, 3.5, 0, plate_w=0.5, gap=0.2)
ax.text(2.9, 1.75, r'$C_\infty = k_\infty$', ha='right', va='center', fontsize=15)

# Rama 3: Singularidad intermedia 1 (L1 y C1 en serie)
dibujar_inductor(ax, 5.0, 3.5, 1.75, n_turns=5, r=0.18)
ax.text(5.25, 2.65, r'$L_1 = \frac{1}{2k_1}$', ha='left', va='center', fontsize=14)
dibujar_capacitor(ax, 5.0, 1.75, 0, plate_w=0.45, gap=0.15)
ax.text(5.25, 0.85, r'$C_1 = \frac{2k_1}{\omega_{p_1}^2}$', ha='left', va='center', fontsize=14)

# Rama 4: Singularidad intermedia n (Ln y Cn en serie)
dibujar_inductor(ax, 7.2, 3.5, 1.75, n_turns=5, r=0.18)
ax.text(7.45, 2.65, r'$L_n = \frac{1}{2k_n}$', ha='left', va='center', fontsize=14)
dibujar_capacitor(ax, 7.2, 1.75, 0, plate_w=0.45, gap=0.15)
ax.text(7.45, 0.85, r'$C_n = \frac{2k_n}{\omega_{p_n}^2}$', ha='left', va='center', fontsize=14)

# Flecha indicadora de admitancia Y(s)
ax.plot([0.4, 0.4], [1.8, -0.8], 'k:', lw=1.5)
ax.annotate('', xy=(1.8, -0.8), xytext=(0.4, -0.8),
            arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))
ax.text(2.0, -0.8, r'$Y(s)$', ha='left', va='center', fontsize=16)

plt.tight_layout()
plt.savefig('foster_ii.png', dpi=300, bbox_inches='tight')
plt.show()
