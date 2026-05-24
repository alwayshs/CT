def solution(progresses, speeds):
    answer = []
    current = 0
    count = 0

    for p, s in zip(progresses, speeds):
        day = (100 - p + s - 1) // s

        if count == 0:
            current = day
            count = 1
        elif day <= current:
            count += 1
        else:
            answer.append(count)
            current = day
            count = 1

    answer.append(count)
    return answer