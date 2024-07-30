def fibo_num(n, m):
    mod_list = [0, 1, 1]
    if n<= 1:
        return mod_list[n % len(mod_list)]
    else:
        previous        = 1
        current         = 1
        while True:
            temp        = current 
            current     = ( previous + current ) % m
            previous    = temp
            if(previous == 0 and current == 1):
                mod_list =  mod_list[:len(mod_list)-1]
                break
            mod_list.append(current)
        r = n % len(mod_list)
        # print("mod_list," , mod_list)
        # print("len of list, ", len(mod_list))
        # print("r," , r)
        return mod_list[r]


[n, m] = list(map(int, input().split()))

if (n < 1 or n > 100000000000000) or (m < 2 or m > 1000):
    [n, m] = list(map(int, input().split()))
else:
    print(fibo_num(n,m))