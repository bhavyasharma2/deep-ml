import math

def sigmoid(z: float) -> float:
	#Your code here
	result = round(1.0 /(1.0 + math.exp(-z)),4)
	return result