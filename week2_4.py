def lcm(a,b):
    r = 1
    ab = a*b
    if a % b == 0:
        r = min(a,b)

    while(a % b != 0):
        r = a % b
        a = b
        b = r
        

    result = int(ab/r)

    return result


if __name__ == "__main__":            
    input1, input2 = map(int, input().split())

    if input1< 1 or input2 <1 or input1 >10000000 or input2 >10000000:
        input1, input2 = map(int, input().split())

    print(lcm(input1, input2))