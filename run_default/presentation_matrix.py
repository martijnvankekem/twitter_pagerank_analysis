from helpers.files import open_file
from helpers.pagerank_default import run

# --- CONSTANTS ---
# Run type, decides the output folder.
RUN_TYPE = "presentation"

# Read normalized CSR matrix from file and load into memory.
A = open_file(RUN_TYPE, "../dataset/twitter7_normalized_csr.npz")
A = A[0:5_000_000, 0:5_000_000]

# Run pagerank algorithm and write result to output file.
print("Starting PageRank.")
v = run(A, RUN_TYPE, 0.85)