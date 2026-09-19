#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 12:58:45 2026

@author: mariano
"""

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(12, 5), dpi=300)
ax.set_xlim(-0.5, 11.5)
ax.set_ylim(-2.0, 3.0)
ax.axis('off')

# Terminales
ax.plot(0, 1.0, 'o', fillstyle='none', color='black', markersize=8, mew=1.5)
ax.plot(0, -1.0, 'o', fillstyle='none', color='black', markersize=8, mew=1.5)

# Riel inferior y flecha de impedancia Z(s)
ax.plot([0.1, 10.5], [-1.0, -1.0], 'k-', lw=1.5)
ax.plot([0.4, 0.4], [0.6, -1.6], 'k:', lw=1.5)
ax.annotate('', xy=(1.8, -1.6), xytext=(0.4, -1.6),
            arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))
ax.text(2.0, -1.6, r'$Z(s)$', ha='left', va='center', fontsize=16)

def draw_h_inductor(ax, x_left, x_right, y, n_turns=4, r=0.18):
    dx = ((x_right - 0.2) - (x_left + 0.2)) / n_turns
    ax.plot([x_left, x_left + 0.2], [y, y], 'k-', lw=1.5)
    ax.plot([x_right - 0.2, x_right], [y, y], 'k-', lw=1.5)
    for i in range(n_turns):
        center_x = (x_left + 0.2) + (i + 0.5) * dx
        theta = np.linspace(0, np.pi, 30)
        ax.plot(center_x - (dx/2) * np.cos(theta), y + r * np.sin(theta), 'k-', lw=1.5)

def draw_h_capacitor(ax, x_left, x_right, y, plate_h=0.45, gap=0.15):
    mid_x = (x_left + x_right) / 2
    ax.plot([x_left, mid_x - gap/2], [y, y], 'k-', lw=1.5)
    ax.plot([mid_x + gap/2, x_right], [y, y], 'k-', lw=1.5)
    ax.plot([mid_x - gap/2, mid_x - gap/2], [y - plate_h/2, y + plate_h/2], 'k-', lw=1.5)
    ax.plot([mid_x + gap/2, mid_x + gap/2], [y - plate_h/2, y + plate_h/2], 'k-', lw=1.5)

def draw_tank(ax, x_start, x_end, y_center, dy=0.65, label_L="", label_C=""):
    ax.plot([x_start, x_start + 0.3], [y_center, y_center], 'k-', lw=1.5)
    ax.plot([x_start + 0.3, x_start + 0.3], [y_center - dy, y_center + dy], 'k-', lw=1.5)
    draw_h_inductor(ax, x_start + 0.3, x_end - 0.3, y_center + dy, n_turns=4, r=0.18)
    if label_L:
        ax.text((x_start + x_end)/2, y_center + dy + 0.35, label_L, ha='center', va='bottom', fontsize=13)
    draw_h_capacitor(ax, x_start + 0.3, x_end - 0.3, y_center - dy, plate_h=0.45, gap=0.15)
    if label_C:
        ax.text((x_start + x_end)/2, y_center - dy - 0.35, label_C, ha='center', va='top', fontsize=13)
    ax.plot([x_end - 0.3, x_end - 0.3], [y_center - dy, y_center + dy], 'k-', lw=1.5)
    ax.plot([x_end - 0.3, x_end], [y_center, y_center], 'k-', lw=1.5)

# Elementos en serie
ax.plot([0.1, 0.8], [1.0, 1.0], 'k-', lw=1.5)
draw_h_capacitor(ax, 0.8, 2.2, 1.0, plate_h=0.5, gap=0.15)
ax.text(1.5, 1.35, r'$C_0 = \frac{1}{k_0}$', ha='center', va='bottom', fontsize=14)

ax.plot([2.2, 2.8], [1.0, 1.0], 'k-', lw=1.5)
draw_h_inductor(ax, 2.8, 4.4, 1.0, n_turns=5, r=0.22)
ax.text(3.6, 1.45, r'$L_\infty = k_\infty$', ha='center', va='bottom', fontsize=14)

ax.plot([4.4, 4.9], [1.0, 1.0], 'k-', lw=1.5)
draw_tank(ax, 4.9, 7.1, 1.0, dy=0.65, 
          label_L=r'$L_1 = \frac{2k_1}{\omega_{p_1}^2}$', 
          label_C=r'$C_1 = \frac{1}{2k_1}$')

ax.plot([7.1, 7.5], [1.0, 1.0], 'k-', lw=1.5)
ax.text(7.85, 1.0, r'$\cdots$', ha='center', va='center', fontsize=18)
ax.plot([8.2, 8.6], [1.0, 1.0], 'k-', lw=1.5)

draw_tank(ax, 8.6, 10.8, 1.0, dy=0.65, 
          label_L=r'$L_n = \frac{2k_n}{\omega_{p_n}^2}$', 
          label_C=r'$C_n = \frac{1}{2k_n}$')

plt.tight_layout()
plt.savefig('foster_i_serie.png', dpi=300, bbox_inches='tight')
plt.show()