import cvxpy as cvx
from cvxpy.reductions.solvers.solving_chain import construct_solving_chain
import numpy as np
np.random.seed(0)
m = 6
n = 5
A = np.random.randn(m,n)
b = np.random.randn(m)
x = cvx.Variable(n)
f0 = cvx.sum_squares(A*x - b)
prob = cvx.Problem(cvx.Minimize(f0))
prob.solve()
print(f0.value)
