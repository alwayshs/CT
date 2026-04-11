import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
P = int(input_data[1])
T = int(input_data[2])

C = 4 * N - 2

k_arr = [0] * (C + 1)
pref = [0] * (C + 1)

for i in range(1, C + 1):
    if i <= 2 * N:
        k_arr[i] = i
    else:
        k_arr[i] = 4 * N - i
    pref[i] = pref[i-1] + k_arr[i]

cycle_sum = pref[C]

full_cycles = (T - 1) // C
rem = (T - 1) % C

S = full_cycles * cycle_sum + pref[rem]

start = S % (2 * N)

k_T = k_arr[(T - 1) % C + 1]

p1 = 2 * P - 2
p2 = 2 * P - 1

dist1 = (p1 - start) % (2 * N)
dist2 = (p2 - start) % (2 * N)

if dist1 < k_T or dist2 < k_T:
    print("Dehet YeonJwaJe ^~^")
else:
    print("Hing...NoJam")