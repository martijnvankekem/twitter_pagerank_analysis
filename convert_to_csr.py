# This script converts the MTX matrix format to CSR (compressed sparse)
from scipy import sparse
import fast_matrix_market as fmm

print("Starting to read MTX file...")
mat = fmm.mmread("dataset/twitter7.mtx")

print("Reading MTX complete. Converting to CSR...")
csr = mat.tocsr()

print("Converting to CSR complete. Writing to file...")
sparse.save_npz("dataset/twitter7_csr.mtx", csr)

print("Done.")