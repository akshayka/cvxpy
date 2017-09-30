from cvxpy import *
import numpy as np

#print 'RMUL'
#x = Variable(3)
#a = np.ones(3)
#obj = Minimize(x.T * a)
#constr = []
#problem = Problem(obj, constr)
#problem.solve()
#print problem.value
#print x.value

print 'LMUL'
x = Variable(3)
a = Constant(np.ones(3))
b = Constant(3)
import pdb; pdb.set_trace()
c = a + b
obj = Minimize(c.T * x)
constr = []
problem = Problem(obj, constr)
b.value = np.ones(3)
problem.solve()
print problem.value
print x.value
