from cvxpy import *

x = Variable(2)
val = np.array([1, 2])
obj = Minimize(sum(x, 0))
constr = [x == val]
problem = Problem(obj, constr)
problem.solve()
