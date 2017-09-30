#!/bin/bash

jupyter nbconvert --to rst $1.ipynb
sed -i -e 's/code:: $/code:: python/g' $1.rst
