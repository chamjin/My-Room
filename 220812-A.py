NUM = int(input())

d = 2

while NUM != 1:
    if NUM % d != 0:
        d += 1
    else:
        NUM //= d
        print(d)