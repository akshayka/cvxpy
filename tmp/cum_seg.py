from cvxpy import *
import numpy as np

x = Variable((2, 2))
obj = Minimize(sum(x, axis=0)[0])
constr = [x == np.array([[-5, -3], [2, 1]])]
problem = Problem(obj, constr)
problem.solve("ECOS")
print problem.value
print x.value
