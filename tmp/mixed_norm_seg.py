from cvxpy import *
import numpy as np

x = Variable((2, 3))
obj = Minimize((mixed_norm(x, 1, 1)))
constr = [x == np.array([[1, 2, 3], [4, 5, 6]])]
problem = Problem(obj, constr)
problem.solve("ECOS")
print problem.value
print x.value
