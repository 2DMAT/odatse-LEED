# Import required libraries
import matplotlib.pyplot as plt  # For plotting
import numpy as np  # For numerical operations

# Load data from ColorMap.txt file
# x, y are coordinates and f is the function value at each point
x,y,f = np.loadtxt("output/ColorMap.txt", unpack=True)

# Create scatter plot with following properties:
# - x,y coordinates from data
# - Color mapped to f values
# - Point size = 100
# - Color range from 0 to 1
# - RdYlBu (Red-Yellow-Blue) colormap
# - Point border width = 2
# - Full opacity
plt.scatter(x, y, c=f, s=100, vmin=0.00, vmax=1.00, cmap='RdYlBu', linewidth=2, alpha=1.0)

# Set axis labels
plt.xlabel("z1")
plt.ylabel("z2")

# Optional: Set axis limits (currently commented out)
#plt.xlim(3.0, 6.5)
#plt.ylim(3.0, 6.5)

# Add colorbar to show mapping between colors and values
plt.colorbar()

# Save figure in both PNG and PDF formats
plt.savefig('ColorMapFig.png')
plt.savefig('ColorMapFig.pdf')
