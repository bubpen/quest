def solution(dots):
    x = []
    y = []
    for i in dots:
        x.append(i[0])
        y.append(i[1])
    
    answer = abs(max(x)- min(x)) * abs(max(y)-min(y))
    return answer