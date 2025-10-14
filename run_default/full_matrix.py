from helpers.files import open_file
from helpers.pagerank_default import run

# --- CONSTANTS ---
# Run type, decides the output folder.
RUN_TYPE = "full"

# Read normalized CSR matrix from file and load into memory.
A = open_file(RUN_TYPE, "../dataset/twitter7_normalized_csr.npz")

# Run pagerank algorithm and write result to output file.
print("Starting PageRank.")
v = run(A, RUN_TYPE, 0.85)