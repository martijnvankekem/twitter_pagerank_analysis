# This script normalizes the matrix and saves it as an additional file
from scipy import sparse
from sklearn.preprocessing import normalize

print("Loading matrix from NPZ...")
A = sparse.load_npz("dataset/twitter7_csr.npz")

print("Normalizing...")
M = normalize(A, norm='l1', axis=0)
print("Normalization finished, writing to file...")

sparse.save_npz("dataset/twitter7_normalized_csr.npz", M)
print("Done.")
