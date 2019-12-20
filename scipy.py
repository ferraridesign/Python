import numpy as np
import pandas as pd
import matplotlib.pylab as plt
my_series = pd.Series([4.6, 2.1, -4.0, 3.0])
print(my_series)

hungarian_dictionary = {'spaceship': 'űrhajó',
                        'watermelon': 'görögdinnye',
                        'bicycle': 'kerékpár'}

# Names (keys) mapped to a tuple (the value) containing the height, lat and longitude.
print("Full table")
scottish_hills = {'Hill Name': ['Ben Nevis', 'Ben Macdui', 'Braeriach', 'Cairn Toul', 'Sgòr an Lochain Uaine'],
                  'Height': [1345, 1309, 1296, 1291, 1258],
                  'Latitude': [56.79685, 57.070453, 57.078628, 57.054611, 57.057999],
                  'Longitude': [-5.003508, -3.668262, -3.728024, -3.71042, -3.725416]}

dataframe = pd.DataFrame(scottish_hills, columns=['Hill Name', 'Height', 'Latitude', 'Longitude'])
print(dataframe)
print(hungarian_dictionary)
print("First 3 of table")
print(dataframe.head(3))
print("Last 2 of table")
print(dataframe.tail(2))
print("row at positions")
print(dataframe.iloc[0])
print(dataframe.iloc[0,0])
print("test")
print("n")
print(dataframe.Height)
print(dataframe["Hill Name"][0])
"""
t = np.linspace(0, 1, 100)
plt.plot(t, t**2)
plt.show()
"""
