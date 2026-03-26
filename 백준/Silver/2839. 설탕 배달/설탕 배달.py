total = int(input())
count = 0
while total > 0 and (total % 5) != 0:
    total -= 3
    count += 1

if total < 0:
    print(-1)
else:
    count += (total // 5)
    print(count)