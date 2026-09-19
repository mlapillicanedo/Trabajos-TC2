#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 13:06:45 2026

@author: mariano
"""

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(12, 5), dpi=300)
ax.set_xlim(-0.5, 12.0)
ax.set_ylim(-1.8, 4.0)
ax.axis('off')

# Terminales de entrada
ax.plot(0, 3.0, 'o', fillstyle='none', color='black', markersize=8, mew=1.5)
ax.plot(0, 0, 'o', fillstyle='none', color='black', markersize=8, mew=1.5)

# Riel inferior y flecha indicadora Z(s)
ax.plot([0.1, 11.2], [0, 0], 'k-', lw=1.5)
ax.plot([0.4, 0.4], [2.2, -0.9], 'k:', lw=1.5)
ax.annotate('', xy=(1.8, -0.9), xytext=(0.4, -0.9),
            arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))
ax.text(2.0, -0.9, r'$Z(s)$', ha='left', va='center', fontsize=16)

def draw_h_capacitor(ax, x_left, x_right, y, plate_h=0.5, gap=0.2):
    mid_x = (x_left + x_right) / 2
    ax.plot([x_left, mid_x - gap/2], [y, y], 'k-', lw=1.5)
    ax.plot([mid_x + gap/2, x_right], [y, y], 'k-', lw=1.5)
    ax.plot([mid_x - gap/2, mid_x - gap/2], [y - plate_h/2, y + plate_h/2], 'k-', lw=1.5)
    ax.plot([mid_x + gap/2, mid_x + gap/2], [y - plate_h/2, y + plate_h/2], 'k-', lw=1.5)

def draw_v_inductor(ax, x, y_top, y_bot, n_turns=5, r=0.20):
    dy = ((y_top - 0.2) - (y_bot + 0.2)) / n_turns
    ax.plot([x, x], [y_top, y_top - 0.2], 'k-', lw=1.5)
    ax.plot([x, x], [y_bot + 0.2, y_bot], 'k-', lw=1.5)
    for i in range(n_turns):
        center_y = (y_top - 0.2) - (i + 0.5) * dy
        theta = np.linspace(-np.pi/2, np.pi/2, 30)
        ax.plot(x + r * np.cos(theta), center_y + (dy/2) * np.sin(theta), 'k-', lw=1.5)

# Rama 1: Capacitor serie C1
ax.plot([0.1, 0.8], [3.0, 3.0], 'k-', lw=1.5)
draw_h_capacitor(ax, 0.8, 2.4, 3.0, plate_h=0.5, gap=0.2)
ax.text(1.6, 3.45, r'$C_1$', ha='center', va='bottom', fontsize=15)

# Rama 2: Inductor paralelo L2
ax.plot([2.4, 3.4], [3.0, 3.0], 'k-', lw=1.5)
draw_v_inductor(ax, 3.4, 3.0, 0, n_turns=5, r=0.20)
ax.text(3.8, 1.5, r'$L_2$', ha='left', va='center', fontsize=15)

# Rama 3: Capacitor serie C3
ax.plot([3.4, 4.2], [3.0, 3.0], 'k-', lw=1.5)
draw_h_capacitor(ax, 4.2, 5.8, 3.0, plate_h=0.5, gap=0.2)
ax.text(5.0, 3.45, r'$C_3$', ha='center', va='bottom', fontsize=15)

# Rama 4: Inductor paralelo L4
ax.plot([5.8, 6.8], [3.0, 3.0], 'k-', lw=1.5)
draw_v_inductor(ax, 6.8, 3.0, 0, n_turns=5, r=0.20)
ax.text(7.2, 1.5, r'$L_4$', ha='left', va='center', fontsize=15)

# Puntos suspensivos (...)
ax.plot([6.8, 7.6], [3.0, 3.0], 'k-', lw=1.5)
ax.text(8.05, 3.0, r'$\cdots$', ha='center', va='center', fontsize=18)
ax.plot([8.5, 9.1], [3.0, 3.0], 'k-', lw=1.5)

# Rama final: Capacitor C_{n-1} e Inductor L_n
draw_h_capacitor(ax, 9.1, 10.5, 3.0, plate_h=0.5, gap=0.2)
ax.text(9.8, 3.45, r'$C_{n-1}$', ha='center', va='bottom', fontsize=15)
ax.plot([10.5, 11.2], [3.0, 3.0], 'k-', lw=1.5)
draw_v_inductor(ax, 11.2, 3.0, 0, n_turns=5, r=0.20)
ax.text(11.6, 1.5, r'$L_n$', ha='left', va='center', fontsize=15)

plt.tight_layout()
plt.savefig('cauer_ii_dc.png', dpi=300, bbox_inches='tight')
plt.show()