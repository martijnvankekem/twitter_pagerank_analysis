import numpy as np
from helpers.analysis import Analysis
from helpers.files import output_to_file

MAX_ITERATIONS = 10_000
QE_EVERY = 3
TOLERANCE = 1e-10

def l1_normalize(v):
    s = np.sum(v)
    return v / s if s != 0 else v

def pagerank_step(a, x, d=0.85):
    """
    One PageRank multiplication with damping
    """
    n = a.shape[0]
    return d * (a @ x) + (1 - d) * (np.ones(n) / n)

def quadratic_extrapolation(a, xk, d=0.85):
    """
    Algorithm 5: Given x^(k) and matrix A (with damping inside step),
    build x^(k+1), x^(k+2), x^(k+3) and return the accelerated x*.

    Source: https://nlp.stanford.edu/pubs/extrapolation.pdf
    """
    # produce three forward iterates
    x1 = l1_normalize(pagerank_step(a, xk, d))
    x2 = l1_normalize(pagerank_step(a, x1, d))
    x3 = l1_normalize(pagerank_step(a, x2, d))

    y1 = x1 - xk
    y2 = x2 - xk
    y3 = x3 - xk

    y = np.column_stack([y1, y2])

    # (gamma1, gamma2)^T = - y^+ y^(k+3), gamma3 = 1
    g12, *_ = np.linalg.lstsq(y, -y3, rcond=None)
    gamma1, gamma2 = g12
    gamma3 = 1.0

    beta0 = gamma1 + gamma2 + gamma3
    beta1 = gamma2 + gamma3
    beta2 = gamma3

    x_star = beta0 * x1 + beta1 * x2 + beta2 * x3

    # keep it a probability vector
    x_star = np.maximum(x_star, 0)
    return l1_normalize(x_star)

# ---------- main power method with periodic QE ----------
def run(m, out_path: str, d: float = 0.85):
    """
    PageRank with power iterations accelerated periodically by Quadratic Extrapolation.

    Parameters
    ----------
    m: numpy array
        adjacency matrix where M_i,j represents the link from 'j' to 'i', such that for all 'j'
        m must be column-stochastic (dangling columns already handled).

    out_path: the output path to write to, either 'full', 'presentation' or 'toy'.

    d: float, optional
        damping factor, by default 0.85

    Returns
    -------
    numpy array
        a vector of ranks such that v_i is the i-th rank from [0, 1],

    Algorithm 6: Power Method with Quadratic Extrapolation
    Source: https://nlp.stanford.edu/pubs/extrapolation.pdf
    """
    analysis_obj = Analysis("pagerank_quadratic",
                            "PageRank algorithm - Quadratic")
    analysis_obj.start()

    n = m.shape[0]
    x = np.ones(n) / n

    k = 0
    while k < MAX_ITERATIONS:
        analysis_obj.start_iteration()
        # standard power step
        x_next = l1_normalize(pagerank_step(m, x, d))
        norm = np.linalg.norm(x_next - x, 1)
        x = x_next
        k += 1

        print("Norm", norm)
        analysis_obj.stop_iteration({"norm": norm})

        # periodically apply QE using current x as x^(k)
        if QE_EVERY and (k % QE_EVERY == 0) and k + 3 <= MAX_ITERATIONS:
            x = quadratic_extrapolation(m, x, d)
            if np.linalg.norm(pagerank_step(m, x, d) - x, 1) < TOLERANCE:
                break

        if norm < TOLERANCE:
            break

    # Finish analysis
    analysis_obj.stop()
    analysis_obj.write_to_file(out_path)

    # Algorithm finished, write to file
    output_to_file(out_path, x)
    return x