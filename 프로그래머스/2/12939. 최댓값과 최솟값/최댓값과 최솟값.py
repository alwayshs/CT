def solution(s):
    s_split = list(map(int, s.split()))
    min, max = s_split[0], s_split[0]
    
    for i in s_split:
        if i < min:
            min = i
        if i > max:
            max = i

    answer = f'{min} {max}'
    return answer