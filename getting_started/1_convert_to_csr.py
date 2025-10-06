# This script converts the MTX matrix format to CSR (compressed sparse)
from scipy import sparse
import fast_matrix_market as fmm

# Read the regular matrix from file into memory.
print("Starting to read MTX file...")
mat = fmm.mmread("../dataset/twitter7.mtx")

# Convert the regular dense matrix to CSR format.
print("Reading MTX complete. Converting to CSR...")
csr = mat.tocsr()

# Write the CSR matrix to a file.
print("Converting to CSR complete. Writing to file...")
sparse.save_npz("../dataset/twitter7_csr.npz", csr)

print("Done.")