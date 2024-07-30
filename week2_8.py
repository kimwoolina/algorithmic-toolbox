def squares_fibo(n):
    n1, n2 = fibo_num(n)
    return (n1*n2) %10

def fibo_num(n):
    mod_list = [0, 1, 1]
    if n<= 1:
        return mod_list[n % len(mod_list)], mod_list[(n+1) % len(mod_list)]
    else:
        previous        = 1
        current         = 1
        while True:
            temp        = current 
            current     = ( previous + current ) % 10
            previous    = temp
            if(previous == 0 and current == 1):
                mod_list =  mod_list[:len(mod_list)-1]
                break
            mod_list.append(current)
        r1 = n % len(mod_list)
        r2 = (n+1) % len(mod_list)
        return mod_list[r1], mod_list[r2]

if __name__ == '__main__':
    n = int(input())

    if (n < 0 or n > 100000000000000):
        n = int(input())
    else:
        print(squares_fibo(n))