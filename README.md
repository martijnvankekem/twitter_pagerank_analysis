# Twitter Pagerank Analysis

## Getting started
1. Retrieve the dataset from https://sparse.tamu.edu/SNAP/twitter7 in Matrix Market format.
   - Extract the dataset to the `dataset` folder.
2. Install the required dependencies: `pip install scipy fast_matrix_market scikit-learn numpy`
3. Run the `convert_to_csr.py` script to convert the MTX file to a compressed sparse format.
   - A file named `twitter7_csr.npz` will be created in the `dataset` folder. This can take a while.
4. Run the `normalize.py` script (in that order) before running `main.py`.
   - A file named `twitter7_normalized_csr.npz` will be created in the `dataset` folder. This can take a while.

## Running the PageRank algorithm
1. Make sure you've followed the steps in [Getting started](#getting-started).
2. Run the `main.py` script.