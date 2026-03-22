total = int(input())
time = list(map(int, input().split()))
var = 0
count = 0
prev = 0

for i in range(total):
    for j in range(len(time) - 1 - i):
        if time[j] > time[j + 1]:
            var = time[j]
            time[j] = time[j + 1]
            time[j + 1] = var

for i in range(total):
    if i == 0:
        count += time[i]
        prev += time[i]
    else:
        count += (time[i] + prev)
        prev += time[i]

print(count)