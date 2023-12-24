import pandas as pd
import math

G = 1.327E11  # Gravitational constant, km^3/s^2
pi = 3.14159  # circumference
M = 2000000  # M is the Black Hole mass, solar masses

distances = []
periods = []

print("The Mass of The Black Hole: ",M," Solar Masses\n")
for dist in range(5000, 1000000, 10000):
    period = 2 * pi * math.sqrt(dist ** 3 / (2.0 * G * M))
    distances.append(dist)
    periods.append(period)

data = {
    'Distance (Kilometers)': distances,
    'Period (seconds)': periods
}

df = pd.DataFrame(data)
print(df)
