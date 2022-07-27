# 백준 4948 (자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램)

# <시간 초과>
# def isPrime(num):
#     if num==1:
#         return False
#     else:
#         for i in range(2, int(num**0.5)+1):
#             if num%i == 0:
#                 return False
#         return True

# while True:

#     N = int(input())
#     LIST = []

#     if N == 0:
#         break

#     for i in range(N, (2*N)+1):
#         if isPrime(i):
#             LIST.append(i)
#     print(len(LIST))

import sys

input = sys.stdin.readline

inputList = list()

N = 123456*2 + 1
isPrime = [True] * N

for i in range(2, int(N**0.5)+1):
    if isPrime[i]:
        for j in range(2*i, N, i):
            isPrime[j] = False


def counting(inputValue):
    cnt = 0
    for k in range(inputValue+1, inputValue*2 + 1):
        if isPrime[k]:
            cnt += 1
    print(cnt)


while True:
    k = int(input())

    if not k:
        break
    counting(k)

# 다른 사람의 코드...