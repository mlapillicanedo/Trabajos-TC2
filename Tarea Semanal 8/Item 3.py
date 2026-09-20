#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 18:54:06 2026

@author: mariano
"""

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(9, 5))

# --- Funciones auxiliares para dibujar componentes y símbolos ---

def draw_port(x, y, label):
    """Dibuja el conector de entrada poligonal con su etiqueta."""
    w, h = 0.5, 0.4
    poly = np.array([
        [x, y - h/2],
        [x + w * 0.7, y - h/2],
        [x + w, y],
        [x + w * 0.7, y + h/2],
        [x, y + h/2]
    ])
    ax.plot(poly[:, 0], poly[:, 1], color='dodgerblue', lw=1.5)
    ax.text(x + w * 0.35, y, label, ha='center', va='center', 
            fontsize=17, fontweight='bold', color='black')

def draw_node(x, y, size=35):
    """Dibuja los nodos de unión como cuadrados azules."""
    ax.scatter([x], [y], s=size, color='blue', marker='s', zorder=5)

def draw_resistor(x, y, orient='h', length=1.4, n_peaks=3, amp=0.25, color='navy', lw=1.3):
    """Dibuja una resistencia en zigzag."""
    lead = 0.25
    body_len = length - 2 * lead
    if orient == 'h':
        xs = [x, x + lead]
        ys = [y, y]
        dx = body_len / (4 * n_peaks)
        curr_x = x + lead
        for i in range(n_peaks):
            xs.extend([curr_x + dx, curr_x + 3 * dx, curr_x + 4 * dx])
            ys.extend([y + amp, y - amp, y])
            curr_x += 4 * dx
        xs.append(x + length)
        ys.append(y)
        ax.plot(xs, ys, color=color, lw=lw)
    else:  # orient == 'v' (hacia abajo)
        xs = [x, x]
        ys = [y, y - lead]
        dy = body_len / (4 * n_peaks)
        curr_y = y - lead
        for i in range(n_peaks):
            xs.extend([x + amp, x - amp, x])
            ys.extend([curr_y - dy, curr_y - 3 * dy, curr_y - 4 * dy])
            curr_y -= 4 * dy
        xs.append(x)
        ys.append(y - length)
        ax.plot(xs, ys, color=color, lw=lw)

def draw_inductor(x, y, orient='h', length=1.6, n_turns=3, r=0.35, color='navy', lw=1.3):
    """Dibuja un inductor mediante arcos consecutivos."""
    step = length / n_turns
    if orient == 'h':
        for i in range(n_turns):
            cx = x + (i + 0.5) * step
            theta = np.linspace(np.pi, 0, 100)
            xs = cx - (step / 2) * np.cos(theta)
            ys = y + r * np.sin(theta)
            ax.plot(xs, ys, color=color, lw=lw)
    else:  # 'v'
        for i in range(n_turns):
            cy = y - (i + 0.5) * step
            theta = np.linspace(np.pi / 2, -np.pi / 2, 100)
            xs = x + r * np.cos(theta)
            ys = cy + (step / 2) * np.sin(theta)
            ax.plot(xs, ys, color=color, lw=lw)

def draw_capacitor(x, y, orient='v', length=1.6, gap=0.28, plate_len=0.75, color='navy', lw=1.4):
    """Dibuja un capacitor de placas paralelas."""
    if orient == 'v':
        # Conexión superior
        ax.plot([x, x], [y, y - (length - gap) / 2], color=color, lw=lw)
        # Placa superior
        ax.plot([x - plate_len / 2, x + plate_len / 2],
                [y - (length - gap) / 2, y - (length - gap) / 2], color=color, lw=lw + 0.5)
        # Placa inferior
        ax.plot([x - plate_len / 2, x + plate_len / 2],
                [y - (length + gap) / 2, y - (length + gap) / 2], color=color, lw=lw + 0.5)
        # Conexión inferior
        ax.plot([x, x], [y - (length + gap) / 2, y - length], color=color, lw=lw)


# --- Armado del circuito ---

y_sup = 3.8
y_inf = 1.0

# Bornes de entrada 1 y 2
draw_port(0.3, y_sup, '1')
draw_port(0.3, y_inf, '2')

# Línea del puerto 1 a R1
ax.plot([0.8, 1.8], [y_sup, y_sup], color='navy', lw=1.2)

# R1 en serie
draw_resistor(1.8, y_sup, orient='h', length=1.4, n_peaks=3)
ax.text(2.5, y_sup + 0.5, 'R1', fontsize=18, fontweight='bold', ha='center')

# Conexión entre R1 y el bloque paralelo R2 || L2
ax.plot([3.2, 3.8], [y_sup, y_sup], color='navy', lw=1.2)
draw_node(3.8, y_sup)

# --- Bloque paralelo R2 || L2 ---
# Rama superior: R2
ax.plot([3.8, 3.8], [y_sup, 4.9], color='red', lw=1.1)
ax.plot([3.8, 4.6], [4.9, 4.9], color='red', lw=1.1)
draw_resistor(4.6, 4.9, orient='h', length=1.4, n_peaks=2)
ax.text(5.3, 5.4, 'R2', fontsize=18, fontweight='bold', ha='center')
ax.plot([6.0, 6.6], [4.9, 4.9], color='red', lw=1.1)
ax.plot([6.6, 6.6], [4.9, y_sup], color='red', lw=1.1)

# Rama inferior: L2
ax.plot([3.8, 4.5], [y_sup, y_sup], color='navy', lw=1.1)
draw_inductor(4.5, y_sup, orient='h', length=1.6, n_turns=3)
ax.text(5.3, y_sup + 0.45, 'L2', fontsize=18, fontweight='bold', ha='center')
ax.plot([6.1, 6.6], [y_sup, y_sup], color='navy', lw=1.1)

# Nodo derecho del bloque paralelo
draw_node(6.6, y_sup)

# Conexión hacia la rama de R3
ax.plot([6.6, 7.5], [y_sup, y_sup], color='navy', lw=1.2)
draw_node(7.5, y_sup)

# Rama en paralelo de R3
draw_resistor(7.5, y_sup, orient='v', length=2.8, n_peaks=3)
ax.text(6.85, 2.4, 'R3', fontsize=18, fontweight='bold', ha='center', va='center')
draw_node(7.5, y_inf)

# Conexión superior hacia C1
ax.plot([7.5, 8.9], [y_sup, y_sup], color='red', lw=1.1)
ax.plot([8.9, 8.9], [y_sup, 3.4], color='red', lw=1.1)

# Capacitor C1 en derivación al extremo derecho
draw_capacitor(8.9, 3.4, orient='v', length=1.4)
ax.text(9.3, 2.7, 'C1', fontsize=18, fontweight='bold', ha='left', va='center')

# Cierre inferior de C1 hacia el nodo inferior de R3
ax.plot([8.9, 8.9], [2.0, y_inf], color='red', lw=1.1)
ax.plot([8.9, 7.5], [y_inf, y_inf], color='red', lw=1.1)

# Retorno inferior desde R3 al puerto 2
ax.plot([7.5, 0.8], [y_inf, y_inf], color='red', lw=1.1)

# --- Ajustes finales de la figura ---
ax.set_xlim(-0.1, 10.0)
ax.set_ylim(0.2, 5.9)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.show()