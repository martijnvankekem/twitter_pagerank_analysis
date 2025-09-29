from scipy import sparse
import numpy as np

# https://en.wikipedia.org/wiki/PageRank#Iterative
def pagerank(M, d: float = 0.85):
    """PageRank algorithm with explicit number of iterations. Returns ranking of nodes (pages) in the adjacency matrix.

    Parameters
    ----------
    A : numpy array
        adjacency matrix where M_i,j represents the link from 'j' to 'i', such that for all 'j'
        The matrix must be normalized first.
    d : float, optional
        damping factor, by default 0.85

    Returns
    -------
    numpy array
        a vector of ranks such that v_i is the i-th rank from [0, 1],

    """
    print("Initializing algorithm...")
    N = M.shape[1]
    w = np.ones(N) / N
    M_hat = d * M
    v = M_hat @ w + (1 - d) / N
    print("Starting iterations.")
    norm = np.linalg.norm(w - v)
    while norm >= 1e-10:
        w = v
        v = M_hat @ w + (1 - d) / N
        norm = np.linalg.norm(w - v)
        print("Norm", norm)
        print(v)
    return v

print("Loading matrix into memory.")
A = sparse.load_npz("dataset/twitter7_normalized_csr.npz")

print("Starting PageRank.")
v = pagerank(A, 0.85)
with open("output.txt", "w") as f:
  f.write(v)
