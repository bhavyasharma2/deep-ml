import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    max_score = max(scores)
    exp_vals = [math.exp(i - max_score) for i in scores]
    sum_exp = sum(exp_vals)
    return [(j / sum_exp) for j in exp_vals]