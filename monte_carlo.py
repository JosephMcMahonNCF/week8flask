import random

def estimate_pi(num_simulations):
    inside_circle = 0

    for _ in range(num_simulations):
        x, y = random.random(), random.random()
        if x*x + y*y <= 0.25:
            inside_circle += 1

    estimated_pi = 4 * (inside_circle / num_simulations)
    return estimated_pi