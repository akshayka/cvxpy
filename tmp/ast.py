import cvxpy

# these are comments
x = cvxpy.Variable(3,
             3) # they better be preserved
y = cvxpy.Bool(5)

z = cvxpy.sum_entries(x)
q = cvxpy.max_elemwise(x, y)

print x
