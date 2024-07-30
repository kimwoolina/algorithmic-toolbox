def fibo_num(n, m):
    if n<= 1:
        return n
    else:
        previous        = 0
        current         = 1
        for a in range(n-1):
            #print("a: ", a)
            #print("current: ", current)
            temp        = current
            current     = ( previous + current ) % m
            previous    = temp
        return current % m


input_numbers = list(map(int, input().split()))

if (input_numbers[0] < 1 or input_numbers[0] > 100000000000000) or (input_numbers[1] < 2 or input_numbers[1] > 1000):
    [n, m] = list(map(int, input().split()))
else:
    print(fibo_num(input_numbers))