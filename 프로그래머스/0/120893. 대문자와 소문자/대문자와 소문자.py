def solution(my_string):
    answer = ''
    for i in my_string:
        if i.upper() == i:
            answer = answer + i.lower()
        else:
            answer = answer + i.upper()
    return answer