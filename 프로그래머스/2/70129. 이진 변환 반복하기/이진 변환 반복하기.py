def solution(s):
    count = 0
    removed = 0

    while s != "1":
        zero_count = s.count("0")
        one_count = len(s) - zero_count

        removed += zero_count
        count += 1

        s = bin(one_count)[2:]

    return [count, removed]