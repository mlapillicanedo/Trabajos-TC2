#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 13:05:27 2026

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

# Riel inferior de retorno y flecha Z(s)
ax.plot([0.1, 11.2], [0, 0], 'k-', lw=1.5)
ax.plot([0.4, 0.4], [2.2, -0.9], 'k:', lw=1.5)
ax.annotate('', xy=(1.8, -0.9), xytext=(0.4, -0.9),
            arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))
ax.text(2.0, -0.9, r'$Z(s)$', ha='left', va='center', fontsize=16)

def draw_h_inductor(ax, x_left, x_right, y, n_turns=4, r=0.22):
    dx = ((x_right - 0.2) - (x_left + 0.2)) / n_turns
    ax.plot([x_left, x_left + 0.2], [y, y], 'k-', lw=1.5)
    ax.plot([x_right - 0.2, x_right], [y, y], 'k-', lw=1.5)
    for i in range(n_turns):
        center_x = (x_left + 0.2) + (i + 0.5) * dx
        theta = np.linspace(0, np.pi, 30)
        ax.plot(center_x - (dx/2) * np.cos(theta), y + r * np.sin(theta), 'k-', lw=1.5)

def draw_v_capacitor(ax, x, y_top, y_bot, plate_w=0.5, gap=0.2):
    mid_y = (y_top + y_bot) / 2
    ax.plot([x, x], [y_top, mid_y + gap/2], 'k-', lw=1.5)
    ax.plot([x, x], [mid_y - gap/2, y_bot], 'k-', lw=1.5)
    ax.plot([x - plate_w/2, x + plate_w/2], [mid_y + gap/2, mid_y + gap/2], 'k-', lw=1.5)
    ax.plot([x - plate_w/2, x + plate_w/2], [mid_y - gap/2, mid_y - gap/2], 'k-', lw=1.5)

# Rama 1: Inductor serie L1
ax.plot([0.1, 0.8], [3.0, 3.0], 'k-', lw=1.5)
draw_h_inductor(ax, 0.8, 2.4, 3.0, n_turns=4, r=0.22)
ax.text(1.6, 3.45, r'$L_1$', ha='center', va='bottom', fontsize=15)

# Rama 2: Capacitor paralelo C2
ax.plot([2.4, 3.4], [3.0, 3.0], 'k-', lw=1.5)
draw_v_capacitor(ax, 3.4, 3.0, 0, plate_w=0.5, gap=0.2)
ax.text(3.75, 1.5, r'$C_2$', ha='left', va='center', fontsize=15)

# Rama 3: Inductor serie L3
ax.plot([3.4, 4.2], [3.0, 3.0], 'k-', lw=1.5)
draw_h_inductor(ax, 4.2, 5.8, 3.0, n_turns=4, r=0.22)
ax.text(5.0, 3.45, r'$L_3$', ha='center', va='bottom', fontsize=15)

# Rama 4: Capacitor paralelo C4
ax.plot([5.8, 6.8], [3.0, 3.0], 'k-', lw=1.5)
draw_v_capacitor(ax, 6.8, 3.0, 0, plate_w=0.5, gap=0.2)
ax.text(7.15, 1.5, r'$C_4$', ha='left', va='center', fontsize=15)

# Continuación (...)
ax.plot([6.8, 7.6], [3.0, 3.0], 'k-', lw=1.5)
ax.text(8.05, 3.0, r'$\cdots$', ha='center', va='center', fontsize=18)
ax.plot([8.5, 9.1], [3.0, 3.0], 'k-', lw=1.5)

# Rama final: Inductor L_{n-1} y Capacitor C_n
draw_h_inductor(ax, 9.1, 10.5, 3.0, n_turns=4, r=0.22)
ax.text(9.8, 3.45, r'$L_{n-1}$', ha='center', va='bottom', fontsize=15)
ax.plot([10.5, 11.2], [3.0, 3.0], 'k-', lw=1.5)
draw_v_capacitor(ax, 11.2, 3.0, 0, plate_w=0.5, gap=0.2)
ax.text(11.55, 1.5, r'$C_n$', ha='left', va='center', fontsize=15)

plt.tight_layout()
plt.savefig('cauer_i.png', dpi=300, bbox_inches='tight')
plt.show()