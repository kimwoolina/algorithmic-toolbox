def fibonacci_sum(n):
    sum_list = [0]
    sum             = 0
    previous        = 0
    current         = 1
    for a in range(n):
        sum = (sum + current)%10
        temp        = current 
        current     = ( previous + current ) % 10
        previous    = temp
        sum_list.append(sum)
        if(sum_list[len(sum_list)-2] == 0 and sum_list[len(sum_list)-1] == 1 and len(sum_list) != 2):
            sum_list = sum_list[:len(sum_list)-2]
            break
    r = n % len(sum_list) 
    return sum_list[r]


if __name__ == '__main__':
    n = int(input())

    if (n < 0 or n > 100000000000000):
        n = int(input())
    else:
        print(fibonacci_sum(n))
