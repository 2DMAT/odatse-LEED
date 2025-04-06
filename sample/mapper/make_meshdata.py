# Import required libraries
import itertools  # For generating cartesian product of arrays
import numpy as np  # For numerical operations

# Create evenly spaced arrays for the two dimensions
x1 = np.linspace(-0.49, 0.51, 11)
x2 = np.linspace(0.7775, 2.7775, 11)

# Generate mesh points by taking cartesian product of x1 and x2
# Print each point with an index starting from 1
# Format: index x1_value x2_value
for i, x in enumerate(itertools.product(x1,x2),1):
    print("{:4d} {:.6f} {:.6f}".format(i, *x))
