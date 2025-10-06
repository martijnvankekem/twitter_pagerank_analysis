# This script normalizes the matrix and saves it as an additional file
from scipy import sparse
from sklearn.preprocessing import normalize

# Load the converted CSR file into memory.
print("Loading matrix from NPZ...")
A = sparse.load_npz("../dataset/twitter7_csr.npz")

# Normalize the array by column using the l1-norm
print("Normalizing...")
M = normalize(A, norm='l1', axis=0)
print("Normalization finished, writing to file...")

# Save the normalized array back to a file.
sparse.save_npz("../dataset/twitter7_normalized_csr.npz", M)
print("Done.")
