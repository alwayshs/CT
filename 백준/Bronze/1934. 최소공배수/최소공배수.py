test_case = int(input())
LCM_list = []
for _ in range(0, test_case):
    N1, N2 = map(int, input().split())
    a, b = N1, N2
    LCM = 0
    while b > 0:
        a, b = b, a % b
    
    LCM = N1 * N2 // a
    LCM_list.append(LCM)

for result in LCM_list:
    print(result)