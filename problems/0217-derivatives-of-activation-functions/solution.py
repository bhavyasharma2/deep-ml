import math
def activation_derivatives(x: float) -> dict[str, float]:
	"""
	Compute the derivatives of Sigmoid, Tanh, and ReLU at a given point x.
	
	Args:
		x: Input value
		
	Returns:
		Dictionary with keys 'sigmoid', 'tanh', 'relu' and their derivative values
	"""
	# Your code here
	sigmoid = 1/(1 + math.exp(-x))
	tanh = math.tanh(x)
	if x > 0:
		relu = 1
	else:
		relu = 0

	result = {
		'sigmoid': sigmoid * (1 - sigmoid),
		'tanh': 1 - tanh**2,
		'relu': relu
	}

	return result