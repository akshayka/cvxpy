#!/bin/bash

make clean; make html; rm -rf /vagrant/cvxpy_docs; cp -R build/html /vagrant/cvxpy_docs
