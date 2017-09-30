#!/bin/bash

for f in *.ipynb; do
    python ../../../cvxpy/utilities/cvxpy_upgrade.py --infile $f --outfile $f
done
