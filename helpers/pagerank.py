import numpy as np
from helpers.analysis import Analysis
from helpers.files import output_to_file


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
    analysis_obj = Analysis("pagerank", "PageRank algorithm")
    analysis_obj.start()

    # Prepare PageRank algorithm
    print("Initializing algorithm...")
    n = m.shape[1]
    w = np.ones(n) / n
    m_hat = d * m

    print("Starting iterations.")
    analysis_obj.start_iteration()
    v = m_hat @ w + (1 - d) / n
    norm = np.linalg.norm(w - v)
    analysis_obj.stop_iteration()
    while norm >= 1e-10:
        # Run another round of the algorithm
        analysis_obj.start_iteration()
        w = v
        v = m_hat @ w + (1 - d) / n
        norm = np.linalg.norm(w - v)

        # Iteration finished, print current norm and result
        print("Norm", norm)
        print(v)
        analysis_obj.stop_iteration()

    # Finish analysis
    analysis_obj.stop()
    analysis_obj.write_to_file(out_path)

    # Algorithm finished, write to file
    output_to_file(out_path, v)
    return v