import sys

input = sys.stdin.readline

nA, nB = map(int, input().split())

set_A = set(map(int, input().split()))

set_B = set(map(int, input().split()))

result = set_A - set_B

if len(result) == 0:
    print(0)
else:
    print(len(result))

    sorted_result = sorted(result)

    print(*sorted_result)