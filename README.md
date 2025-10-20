# Twitter Pagerank Analysis
Group 7 - Scientific computing (Eindhoven University of Technology)

Casper von Berg, Bram Gerrits, Martijn van Kekem, Pax Mallee, Lieke van der Sommen

## Prerequisites
This code requires Python 3.12.0, including the following dependencies (installable via PIP):
- scipy
- fast_matrix_market
- numpy
- scikit-learn

In order to run this code, at least 40 GB of available memory is required in order to process the dataset.
The code is tested on Microsoft Windows 11 Pro Version 10.0.26100 Build 26100. 
We can not guarantee successful execution on other platforms.

## Getting started
1. Retrieve the dataset from https://sparse.tamu.edu/SNAP/twitter7 in Matrix Market format.
   - Extract the dataset to the `dataset` folder.
2. Install the required dependencies: `pip install scipy fast_matrix_market scikit-learn numpy`
3. Run the `getting_started/1_convert_to_csr.py` script to convert the MTX file to a compressed sparse format.
   - A file named `twitter7_csr.npz` will be created in the `dataset` folder. This can take a while.
4. Run the `getting_started/2_normalize.py` script to normalize the CSR matrix.
   - A file named `twitter7_normalized_csr.npz` will be created in the `dataset` folder. This can take a while.
5. Run the `getting_started/3_create_presentation_matrix.py` script to create a submatrix for presentation purposes.
   - A file named `twitter7_normalized_csr_presentation.npz` will be created in the `dataset` folder. This can take a while.

## Running the PageRank algorithm
1. Make sure you've followed the steps in [Getting started](#getting-started).
2. Run the desired script.
   - If you're interested in the full list of PageRank results, instead of just the top 10 min and max, include the CLI argument `--full`.

## Output files
Depending on the script that is run, the output will be stored in a subfolder of the `output/` folder.

- `toy`: the toy example matrix for testing purposes.
- `presentation`: the presentation matrix, which contains a representative slice of the total matrix to simulate results in a faster way.
- `full`: the full matrix, containing all available edges.

After completion of the script, the output folder will contain the following files:
- `top10.txt`: a file with the score of the top-10 best-performing and top-10 worst-performing persons.
- `analysis/matrix_load.txt`: a file with the run-time and complexity analysis for loading the matrix into memory.
- `analysis/pagerank.txt`: a file with the run-time and complexity analysis for executing the PageRank algorithm.