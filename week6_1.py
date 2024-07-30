from sys import stdin

def maximum_gold(capacity, weights):
    weight = len(weights)
    val_arr = [[0 for _ in range(capacity + 1)] for _ in range(weight + 1)]
    
    for w in range(1, weight + 1):
        for i in range(1, capacity + 1):
            val_arr[w][i] = val_arr[w-1][i]
            if weights[w-1] <= i:
                val = val_arr[w-1][i-weights[w-1]] + weights[w-1]
                if val > val_arr[w][i]:
                    val_arr[w][i] = val
    
    return val_arr[weight][capacity]

if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
