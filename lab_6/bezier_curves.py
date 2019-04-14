import matplotlib.pyplot as plt
from svg.path import Path, Line, CubicBezier, parse_path
import numpy as np

d = "m 108.1012,63.032737 c -12.242524,0.08342 -21.730025,1.897112 -32.127986,5.669644 0,0 -21.733632,6.047617 -27.78125,17.764881 -6.134296,11.885196 -3.023809,23.812498 -3.023809,23.812498 0,0 2.456844,15.11905 14.174105,15.49703 11.717263,0.37797 -0.389875,-8.64617 10.772321,-11.1503 12.516138,-2.80787 28.460967,0.26521 21.355656,16.06398 l -5.480655,9.44941 c -6.417548,9.30923 -8.794677,12.14636 -11.90625,17.3869 -7.181548,12.09524 -8.315477,21.54465 -8.315477,24.56846 0,3.02381 -3.401783,17.00892 11.717262,22.67857 15.119049,5.66964 30.238093,2.26785 30.238093,2.26785"
# d = "m 176.40975,31.808861 c 0,0 -13.60545,-1.383604 -18.44808,-0.4612 -4.84262,0.922404 -1.8448,0.691803 -1.8448,0.691803 0,0 10.83825,1.614208 12.45245,22.829496 0.61457,8.077282 0.6918,14.989064 0.6918,14.989064 0,0 0,-5.303822 -21.21529,-6.687428 -21.21529,-1.383605 -35.97375,7.609833 -45.42839,13.605458 -9.45464,5.995627 -17.064474,25.366106 -17.064474,25.366106 0,0 -8.532237,37.58797 16.833874,62.26227 25.36611,24.67431 49.5792,19.83169 49.5792,19.83169 0,0 10.37706,-2.30602 12.91367,-6.22623 2.53661,-3.92022 5.99562,2.53661 5.99562,2.53661 l 1.38361,-5.76502 4.61202,5.99562 v -6.45683 l -0.2306,0.2306"
path = parse_path(d)
points_curve = np.array(np.linspace(0.0, 1.0, num=10))
curves = np.empty((len(path), len(points_curve), 2))
for j, el in enumerate(path):
    for k,i in enumerate(points_curve):
        curves[j][k] = np.array([el.point(i).real, el.point(i).imag])


# My realization of besiar curves
points_arr = np.array([[108.1, 63.0],
                       [95.9, 63.1],
                       [86.4, 64.9],
                       [75.9, 68.7],
                       [75.973, 68.702],
                       [75.973, 68.702],
                       [54.239, 74.749],
                       [48.191, 86.467]])

def cubic_bezier(t, P_, i) :
    return (1 - t)**3 * P_[i] + 3*(1 - t)**2 * t * P_[i+1] + 3*(1-t)*(t**2)*P_[i+2] + (t**3)*P_[i+3]

t = np.array(np.linspace(0.0, 1.0, num=10))
arr_ = np.empty((2*len(t),2))
for k in range(0, len(points_arr), 4):
    for i, el in enumerate(t):
        arr_[i + int(k/4)*len(t)] = cubic_bezier(el, points_arr, k)

def get_data() :
    return curves.reshape(curves.shape[0]*curves.shape[1], curves.shape[2])
