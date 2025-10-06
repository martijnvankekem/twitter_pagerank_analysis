from helper.pagerank import run, open_file

# Define the size of the slice of the total matrix.
SLICE_SIZE = 10000

# Read normalized CSR matrix from file and load into memory.
A = open_file("dataset/twitter7_normalized_csr.npz")
A_cut = A[0:SLICE_SIZE, 0:SLICE_SIZE]

# Run pagerank algorithm and write result to output file.
print("Starting PageRank.")
v = run(A_cut, "presentation", 0.85)