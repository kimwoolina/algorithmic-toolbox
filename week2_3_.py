def gcd(a,b):
    gcd = 1
    for c in range(min(a,b), 0, -1):
        #print("c", c)
        #print("a%c = ", a%c)
        #print("b%c = " , b%c)
        if a%c == 0 and b%c == 0:
            gcd = c
            return gcd
    return gcd


if __name__ == "__main__":            
    input1, input2 = map(int, input().split())

    if input1< 1 or input2 <1 or input1 >2*1000000000 or input2 >2*1000000000:
        input1, input2 = map(int, input().split())

    print(gcd(input1, input2))