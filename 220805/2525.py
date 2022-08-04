a, b = map(int, input().split())
c = int(input())
h = a+((b+c)//60)
if h >= 24:
    print(h-24, (b+c)%60)
else:
    print(h, (b+c)%60)