import numpy as np

# Read the CSV file (semicolon-delimited)
data = np.genfromtxt('receiver_output.csv', delimiter=';', skip_header=1)

# Extract columns
t = data[:, 0]
V = data[:, 1]

# Write arrays to a txt file in Python/Numpy array format
with open('receiver_output_arrays.txt', 'w') as f:
    f.write('t = np.array([' + ', '.join(f'{val:.4g}' for val in t) + '])\n')
    f.write('V = np.array([' + ', '.join(f'{val:.4g}' for val in V) + '])\n')

print("Arrays have been written to receiver_output_arrays.txt")

