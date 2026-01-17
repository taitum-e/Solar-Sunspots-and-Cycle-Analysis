import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

sunspots_df = pd.read_csv('data/monthly-sunspots.csv')

# Make Month column readable by pandas
sunspots_df['Date'] = pd.to_datetime(sunspots_df['Month'], format='%Y-%m')

sunspots_x = sunspots_df['Date'].values
sunspots_y = sunspots_df['Sunspots'].values

peaks, properties = find_peaks(sunspots_y, 
                               prominence=40, 
                               distance=120)

# Cycle lengths, x and y
cycle_lengths = np.diff(peaks)
cycle_lengths_x = peaks[1:]

# Plot graphs
fig, (ax1, ax2) = plt.subplots(1,2, figsize=(14,7), dpi=100)

ax1.plot(sunspots_x, 
         sunspots_y, 
         label='Observed Sunspots', 
         color='blue')

ax1.grid(True, 
         linestyle='--', 
         alpha=0.8)

ax1.set_title('Observed Sunspots')

ax2.plot(cycle_lengths_x, 
         cycle_lengths, 
         '-o', 
         label='Cycle Length', 
         color='orange')

ax2.grid(True, 
         linestyle='--', 
         alpha=0.8)

ax2.set_title('Solar Cycle Lengths')

fig.canvas.manager.set_window_title('Observed Sunspots & Change in Solar Cycle Length')

plt.show()
