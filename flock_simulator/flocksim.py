import math
import numpy as np
import matplotlib as plt

width, height = 640, 480
N = 10

positions = [width/2.0, height/2.0] + 10*np.random.rand(2*N).reshape(N, 2)
angles = 2*math.pi*np.random.rand(N)
velocities = np.array(list(zip(np.sin(angles), np.cos(angles))))


def apply_boundary_conditions(self):
    """apply boundary conditions"""
    edge_buffer_radius = 2.0
    for position in self.positions:
        x = position[0]
        y = position[1]

        if x > width + edge_buffer_radius:
            x = - edge_buffer_radius
        elif x < - edge_buffer_radius:
            x = width + edge_buffer_radius

        if y > height + edge_buffer_radius:
            y = - edge_buffer_radius
        elif y < - edge_buffer_radius:
            y = height + edge_buffer_radius

        position[0] = x
        position[1] = y


figure = plt.figure()
axes = plt.axes(xlim=(0, width), ylim=(0, height))

bird_bodies, = axes.plot([], [], markersize=10, c='k', marker='o', ls='None')

#TODO Pick up here from page 76, code line 2 beak == bird_beak





