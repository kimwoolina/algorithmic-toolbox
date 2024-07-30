def fibo_num(n):
    if n<= 1:
        return n
    else:
        fibo_list = [0, 1]
        #print("len of list: " , len(fibo_list))
        if len(fibo_list) <= n:
            for a in range(n+1):
                if a > 1:
                    fibo_n = fibo_list[a-2] + fibo_list[a-1]
                    fibo_list.append(fibo_n)
            #print("fibo_list: " , fibo_list)
    return fibo_list[n]


input_number = int(input())

if input_number < 0 or input_number > 45:
    input_number = int(input())
else:
    print(fibo_num(input_number))