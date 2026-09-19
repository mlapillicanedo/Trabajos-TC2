#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 21:37:59 2026

@author: mariano
"""

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(9, 6))

# --- Funciones auxiliares para componentes ---

def draw_capacitor(x, y, orient='h', length=1.2, gap=0.3, plate_len=0.8, color='navy', lw=1.5):
    """Dibuja un capacitor con sus placas."""
    if orient == 'h':
        # Conexión izquierda
        ax.plot([x, x + (length - gap)/2], [y, y], color=color, lw=lw)
        # Placa 1
        ax.plot([x + (length - gap)/2, x + (length - gap)/2], 
                [y - plate_len/2, y + plate_len/2], color=color, lw=lw + 0.5)
        # Placa 2
        ax.plot([x + (length + gap)/2, x + (length + gap)/2], 
                [y - plate_len/2, y + plate_len/2], color=color, lw=lw + 0.5)
        # Conexión derecha
        ax.plot([x + (length + gap)/2, x + length], [y, y], color=color, lw=lw)
    else:  # 'v' vertical
        # Conexión superior
        ax.plot([x, x], [y, y - (length - gap)/2], color=color, lw=lw)
        # Placa 1
        ax.plot([x - plate_len/2, x + plate_len/2], 
                [y - (length - gap)/2, y - (length - gap)/2], color=color, lw=lw + 0.5)
        # Placa 2
        ax.plot([x - plate_len/2, x + plate_len/2], 
                [y - (length + gap)/2, y - (length + gap)/2], color=color, lw=lw + 0.5)
        # Conexión inferior
        ax.plot([x, x], [y - (length + gap)/2, y - length], color=color, lw=lw)

def draw_inductor(x, y, orient='h', length=1.8, n_turns=4, r=0.25, color='navy', lw=1.3):
    """Dibuja una bobina/inductor mediante semicírculos o arcos continuos."""
    step = length / n_turns
    if orient == 'h':
        for i in range(n_turns):
            cx = x + (i + 0.5) * step
            theta = np.linspace(np.pi, 0, 100)
            xs = cx - (step/2) * np.cos(theta)
            ys = y + r * np.sin(theta)
            ax.plot(xs, ys, color=color, lw=lw)
    else:  # 'v' vertical
        for i in range(n_turns):
            cy = y - (i + 0.5) * step
            theta = np.linspace(np.pi/2, -np.pi/2, 100)
            xs = x + r * np.cos(theta)
            ys = cy + (step/2) * np.sin(theta)
            ax.plot(xs, ys, color=color, lw=lw)

def draw_port(x, y, label, label_offset=0.2):
    """Dibuja el conector en forma de flecha/puerto característico."""
    w, h = 0.5, 0.4
    poly = np.array([
        [x, y - h/2],
        [x + w*0.7, y - h/2],
        [x + w, y],
        [x + w*0.7, y + h/2],
        [x, y + h/2]
    ])
    ax.plot(poly[:, 0], poly[:, 1], color='dodgerblue', lw=1.5)
    ax.text(x + w*0.35, y, label, ha='center', va='center', 
            fontsize=18, fontweight='bold', color='black')

def draw_node(x, y, size=35):
    """Dibuja los nodos de conexión como cuadrados azules."""
    ax.scatter([x], [y], s=size, color='blue', marker='s', zorder=5)

# --- Construcción del Circuito ---

# Puerto 1 (superior) y 2 (inferior)
draw_port(0.2, 4.0, '1')
draw_port(0.2, 1.0, '2')

# Línea del puerto 1 a C1
ax.plot([0.7, 1.3], [4.0, 4.0], color='navy', lw=1.3)

# C1
draw_capacitor(1.3, 4.0, orient='h', length=1.2)
ax.text(1.9, 4.4, 'C1', fontsize=18, fontweight='bold', ha='center')

# Línea de C1 al nodo intermedio
ax.plot([2.5, 3.2], [4.0, 4.0], color='red', lw=1.2)
draw_node(3.2, 4.0)

# Rama L1 (vertical)
ax.plot([3.2, 3.2], [4.0, 3.5], color='red', lw=1.2)
draw_inductor(3.2, 3.5, orient='v', length=1.6, n_turns=3, r=0.35)
ax.plot([3.2, 3.2], [1.9, 1.0], color='red', lw=1.2)
ax.text(3.75, 2.7, 'L1', fontsize=18, fontweight='bold', ha='center', va='center')

draw_node(3.2, 1.0)

# Línea de retorno al Puerto 2
ax.plot([0.7, 3.2], [1.0, 1.0], color='red', lw=1.2)

# Conexión hacia el tanque resonante paralelo (L2 || C2)
ax.plot([3.2, 4.4], [4.0, 4.0], color='red', lw=1.2)
draw_node(4.4, 4.0)

# Ramas del tanque
# Rama L2 (superior)
ax.plot([4.4, 4.6], [4.0, 5.1], color='red', lw=1.2)
ax.plot([4.6, 4.8], [5.1, 5.1], color='red', lw=1.2)
draw_inductor(4.8, 5.1, orient='h', length=1.6, n_turns=3, r=0.4)
ax.plot([6.4, 6.6], [5.1, 5.1], color='red', lw=1.2)
ax.plot([6.6, 6.8], [5.1, 4.0], color='red', lw=1.2)
ax.text(5.6, 5.6, 'L2', fontsize=18, fontweight='bold', ha='center')

# Rama C2 (inferior)
ax.plot([4.4, 4.6], [4.0, 3.4], color='red', lw=1.2)
ax.plot([4.6, 5.0], [3.4, 3.4], color='red', lw=1.2)
draw_capacitor(5.0, 3.4, orient='h', length=1.2, plate_len=0.7)
ax.plot([6.2, 6.6], [3.4, 3.4], color='red', lw=1.2)
ax.plot([6.6, 6.8], [3.4, 4.0], color='red', lw=1.2)
ax.text(5.6, 3.85, 'C2', fontsize=18, fontweight='bold', ha='center')

draw_node(6.8, 4.0)

# Conexión hacia C3
ax.plot([6.8, 8.4], [4.0, 4.0], color='red', lw=1.2)
ax.plot([8.4, 8.4], [4.0, 3.2], color='red', lw=1.2)

# C3 (vertical)
draw_capacitor(8.4, 3.2, orient='v', length=1.4, plate_len=0.8)
ax.text(7.85, 2.5, 'C3', fontsize=18, fontweight='bold', ha='center', va='center')

# Cierre inferior hacia C3
ax.plot([8.4, 8.4], [1.8, 1.0], color='navy', lw=1.2)
ax.plot([3.2, 8.4], [1.0, 1.0], color='red', lw=1.2)

# --- Ajustes de vista ---
ax.set_xlim(-0.2, 9.2)
ax.set_ylim(0.2, 6.2)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.show()