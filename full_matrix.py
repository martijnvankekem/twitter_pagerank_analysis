from helper.pagerank import run, open_file

# Read normalized CSR matrix from file and load into memory.
A = open_file("dataset/twitter7_normalized_csr.npz")

# Run pagerank algorithm and write result to output file.
print("Starting PageRank.")
v = run(A, "full", 0.85)