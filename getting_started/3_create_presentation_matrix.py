# This script loads the huge Twitter7 dataset and saves a submatrix to file for presentation purposes.
from scipy import sparse

SLICE_SIZE = 5_000_000

print("Loading matrix from NPZ...")
A = sparse.load_npz("../dataset/twitter7_normalized_csr.npz")

print("Creating submatrix...")
A_cut = A[0:SLICE_SIZE, 0:SLICE_SIZE]
print("Creating submatrix finished, writing to file...")

# Save the normalized array back to a file.
sparse.save_npz("../dataset/twitter7_normalized_csr_presentation.npz", A_cut)
print("Done.")