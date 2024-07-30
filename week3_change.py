def change(money):
    cnt = 0
    amt = money

    while amt >= 10:
        amt -= 10
        cnt += 1
        
    while amt >= 5:
        amt -= 5
        cnt += 1

    while amt >= 1:
        amt -= 1
        cnt += 1
    return cnt


if __name__ == '__main__':
    m = int(input())
    if m < 1 or m > 1000:
        m = int(input())
    else:
       print(change(m))
