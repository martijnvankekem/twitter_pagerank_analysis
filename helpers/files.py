import sys

import numpy as np
from scipy import sparse
from helpers.analysis import Analysis

def output_to_file(out_path, array):
    """ Write the given numpy array to a text file.

    Parameters
    ----------
    out_path: the output path to write to, either 'full' or 'presentation'
    array: the array to write.
    """
    print("Sorting PageRank values.")
    sorted_array = np.sort(array)
    print("Values sorted, writing output to files.")

    # Save top 10 lowest and highest values.
    with open("output/" + out_path + "/top10.txt", "wb") as f:
        f.write(b"Top 10 - Lowest values\n")
        np.savetxt(f, sorted_array[0:10], delimiter="\n")

        f.write(b"\n\nTop 10 - Highest values\n")
        np.savetxt(f, sorted_array[-10:], delimiter="\n")

    # If CLI argument '--full' is supplied, also write full output to files.
    if len(sys.argv) >= 2 and sys.argv[1] == "--full":
        # Save complete unsorted output.
        with open("output/" + out_path + "/full_unsorted.txt", "wb") as f:
            f.write(b"COMPLETE - Unsorted\n")
            np.savetxt(f, array, delimiter="\n")

        # Save complete sorted output.
        with open("output/" + out_path + "/full_sorted.txt", "wb") as f:
            f.write(b"COMPLETE - Sorted\n")
            np.savetxt(f, sorted_array, delimiter="\n")


def open_file(out_path: str, filename):
    """Function that opens the NPZ matrix file and loads it into memory.

    Parameters
    ----------
    out_path: the output path to write to, either 'full' or 'presentation'.
    filename: the name of the file relative to the current working directory.

    Returns
    -------
    The matrix that has been loaded into memory.

    """
    # Start analysis
    analysis_obj = Analysis("matrix_load", "Loading matrix into memory")
    analysis_obj.start()

    print("Loading matrix into memory.")
    result = sparse.load_npz(filename)

    # Stop analysis
    analysis_obj.stop()
    analysis_obj.write_to_file(out_path)
    return result