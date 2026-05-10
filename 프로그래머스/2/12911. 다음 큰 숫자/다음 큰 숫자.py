def solution(n):
    target_count = bin(n).count("1")

    num = n + 1

    while True:
        if bin(num).count("1") == target_count:
            return num

        num += 1