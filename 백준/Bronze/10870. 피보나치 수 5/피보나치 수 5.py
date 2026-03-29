def fibonacci(n):
    if n <= 1:
        return n
    
    result = 0
    prev = 0
    next = 1
    
    for i in range(2, n + 1):
        result = prev + next
        prev = next
        next = result
    return result

val = int(input())
print(fibonacci(val))