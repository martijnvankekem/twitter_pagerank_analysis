import numpy as np
from scipy import sparse


# https://en.wikipedia.org/wiki/PageRank#Iterative
def run(m, out_path: str, d: float = 0.85):
    """PageRank algorithm with explicit number of iterations. Returns ranking of nodes (pages) in the adjacency matrix.

    Parameters
    ----------
    m: numpy array
        adjacency matrix where M_i,j represents the link from 'j' to 'i', such that for all 'j'
        The matrix must be normalized first.

    out_path: the output path to write to, either 'full' or 'presentation'

    d: float, optional
        damping factor, by default 0.85

    Returns
    -------
    numpy array
        a vector of ranks such that v_i is the i-th rank from [0, 1],

    """
    # Prepare PageRank algorithm
    print("Initializing algorithm...")
    n = m.shape[1]
    w = np.ones(n) / n
    m_hat = d * m

    print("Starting iterations.")
    v = m_hat @ w + (1 - d) / n
    norm = np.linalg.norm(w - v)
    while norm >= 1e-10:
        # Run another round of the algorithm
        w = v
        v = m_hat @ w + (1 - d) / n
        norm = np.linalg.norm(w - v)

        # Iteration finished, print current norm and result
        print("Norm", norm)
        print(v)

    # Algorithm finished, write to file
    output_to_file(out_path, v)
    return v

def output_to_file(out_path, array):
    """ Write the given numpy array to a text file.

    Parameters
    ----------
    out_path: the output path to write to, either 'full' or 'presentation'
    array: the array to write.
    """
    # Write complete array to file
    sorted_array = np.sort(array)
    with open("output/" + out_path + "/top10.txt", "ab") as f:
        f.write(b"Top 10 - Lowest values\n")
        np.savetxt(f, sorted_array[0:10])

        f.write(b"\n\nTop 10 - Highest values\n")
        np.savetxt(f, sorted_array[-10:])

    with open("output/" + out_path + "/full_unsorted.txt", "ab") as f:
        f.write(b"COMPLETE - Unsorted\n")
        np.savetxt(f, array, delimiter="\n")

    with open("output/" + out_path + "/full_sorted.txt", "ab") as f:
        f.write(b"COMPLETE - Sorted\n")
        np.savetxt(f, sorted_array, delimiter="\n")

def open_file(filename):
    """Function that opens the NPZ matrix file and loads it into memory.

    Parameters
    ----------
    filename: the name of the file relative to the current working directory.

    Returns
    -------
    The matrix that has been loaded into memory.

    """
    print("Loading matrix into memory.")
    return sparse.load_npz(filename)