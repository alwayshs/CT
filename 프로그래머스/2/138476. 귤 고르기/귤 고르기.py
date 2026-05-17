from collections import Counter

def solution(k, tangerine):
    answer = 0

    for count in sorted(Counter(tangerine).values(), reverse=True):
        k -= count
        answer += 1

        if k <= 0:
            break

    return answer