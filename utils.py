def generate_array(min_val, max_val, size):
    import random
    return [random.randint(min_val, max_val) for _ in range(size)]

