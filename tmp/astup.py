import cvxpy

# these are comments
x = cvxpy.Variable(shape=(3, 3)) # they better be preserved
y = cvxpy.Variable(shape=(5,1), boolean=True)

z = cvxpy.sum(x)
q = cvxpy.max(x, y)

print x
