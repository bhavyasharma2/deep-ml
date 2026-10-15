import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
	x = np.array(scores)
	c = np.max(x)
	scaled_x = x - c
	log_sum_exp = np.log(np.sum(np.exp(scaled_x)))
	return scaled_x - log_sum_exp