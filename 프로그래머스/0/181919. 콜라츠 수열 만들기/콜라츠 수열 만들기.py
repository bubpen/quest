def solution(n):
    answer = []
    while n != 1:
        answer.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        if n == 1:
            answer.append(n)
    return answer