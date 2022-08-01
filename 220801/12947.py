def solution(x):
    if x % sum(map(int, str(x))) == 0:
        return True
    else:
        return False

print(solution(int(input())))
