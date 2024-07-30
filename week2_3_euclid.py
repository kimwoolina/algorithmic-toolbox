def gcd(a,b):
    r = 1
    if a % b == 0:
        r = min(a,b)

    while(a % b != 0):
        r = a % b
        a = b
        b = r
        
    return r


if __name__ == "__main__":            
    input1, input2 = map(int, input().split())

    if input1< 1 or input2 <1 or input1 >2*1000000000 or input2 >2*1000000000:
        input1, input2 = map(int, input().split())

    print(gcd(input1, input2))