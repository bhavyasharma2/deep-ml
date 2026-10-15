import math
def softmax_derivative(x: list[float]) -> list[list[float]]:
	"""
	Compute the Jacobian matrix of the softmax function.
	
	Args:
		x: Input vector of real numbers
		
	Returns:
		Jacobian matrix J where J[i][j] = d(softmax_i)/d(x_j)
	"""
	# Your code here
	max_x = max(x)
	exp_x = [math.exp(xi - max_x) for xi in x]
	total = sum(exp_x)
	s = [val / total for val in exp_x]
	n = len(s)
	j = [[0.0]* n for _ in range(n)]
	for i in range(n):
		for k in range(n):
			if i == k:
				j[i][k] = s[i] * (1 -s[i])
			else:
				j[i][k] = -s[i] * s[k]

	return j