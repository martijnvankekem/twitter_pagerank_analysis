from helpers.files import open_file
from helpers.pagerank import run

# --- CONSTANTS ---
# Slice size of total matrix for presentation purposes.
SLICE_SIZE = 5_000_000
# Run type, decides the output folder.
RUN_TYPE = "presentation"

# Read normalized CSR matrix from file and load into memory.
A = open_file(RUN_TYPE, "dataset/twitter7_normalized_csr.npz")
A_cut = A[0:SLICE_SIZE, 0:SLICE_SIZE]

# Run pagerank algorithm and write result to output file.
print("Starting PageRank.")
v = run(A_cut, RUN_TYPE, 0.85)