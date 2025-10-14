import numpy as np
from sklearn.preprocessing import normalize
from helpers.pagerank_quadratic import run
import matplotlib.pyplot as plt

# --- CONSTANTS ---
# Run type, decides the output folder.
RUN_TYPE = "toy"

# Read toy example
toy_example = np.array([
    [0.00, 1.00, 0.00, 0.00, 1.00, 0.00, 1.00, 0.00, 1.00, 0.00],
    [1.00, 0.00, 1.00, 0.00, 1.00, 0.00, 1.00, 0.00, 1.00, 1.00],
    [1.00, 0.00, 0.00, 1.00, 1.00, 0.00, 1.00, 0.00, 1.00, 1.00],
    [1.00, 1.00, 0.00, 0.00, 0.00, 0.00, 1.00, 1.00, 1.00, 1.00],
    [0.00, 0.00, 1.00, 1.00, 0.00, 1.00, 1.00, 0.00, 1.00, 0.00],
    [0.00, 0.00, 0.00, 1.00, 0.00, 1.00, 0.00, 0.00, 1.00, 1.00],
    [0.00, 0.00, 0.00, 0.00, 1.00, 0.00, 0.00, 1.00, 1.00, 1.00],
    [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 1.00, 1.00, 0.00],
    [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 1.00, 0.00],
    [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 1.00, 0.00],
])

# Normalize matrix
A = normalize(toy_example, norm='l1', axis=0)

# Run pagerank algorithm and write result to output file.
print("Starting PageRank.")
v = run(A, RUN_TYPE, 0.85)
plt.bar(range(0,10), v)
plt.show()