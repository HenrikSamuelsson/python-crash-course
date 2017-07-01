# 15-1. Cubes

import matplotlib.pyplot as plt

def plot_cubes(min_x, max_x):
	"""Plots the cube of range of numbers"""
	x_values = list(range(min_x, max_x))
	y_values = [x**3 for x in x_values]

	plt.scatter(x_values, y_values, s = 40)
	plt.show()

start_x = 1
stop_x = 6
plot_cubes(start_x, stop_x)

start_x = 1
stop_x = 5001
plot_cubes(start_x, stop_x)
