# Compute Oribital Time Period of Binary Black Holes #
import math

G = 1.327E11 # Gravitational constant, km^3/s^2 #
pi = 3.14159 # circumference #
period = 0 # Orbital period #
M = 20 # M is the BH mass in solar masses #
dist = 10000 # The distance between two black holes, Km #

for dist in range(5000, 100000, 1000):
    # dist = dist + 100000
    period = 2 * pi * math.sqrt(dist ** 3 / (2.0 * G * M))
    print(f"{dist} Kilometers, {period} seconds")
