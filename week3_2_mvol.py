from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.
    weight_and_val = []
    
    for i in range(len(weights)):
        weight_and_val.append((weights[i], values[i]/weights[i]))

    weight_and_val = sorted(weight_and_val, key=lambda x: x[1], reverse=True)

    while capacity != 0 and len(weight_and_val) != 0:
        weight, max_val = weight_and_val.pop(0)

        if capacity < weight:
            value += capacity * max_val
            capacity = 0
        else:
            value += weight*max_val
            capacity -= weight
    
    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
