def fibo_num(n):
    if n<= 1:
        return n
    else:
        previous        = 0
        current         = 1
        for a in range(n-1):
            temp        = current
            current     = (previous + current) % 10
            previous    = temp
    return current%10


input_number = int(input())

if input_number < 0 or input_number > 1000000:
    input_number = int(input())
else:
    print(fibo_num(input_number))