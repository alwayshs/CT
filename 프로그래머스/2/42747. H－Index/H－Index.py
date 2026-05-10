def solution(citations):
    citations.sort(reverse=True)

    answer = 0

    for i, citation in enumerate(citations):
        h = i + 1

        if citation >= h:
            answer = h
        else:
            break

    return answer