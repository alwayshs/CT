def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for i in range(len(numbers) - 1, -1, -1):
        num = numbers[i]
    
        while stack and stack[-1] <= num:
            stack.pop()
    
        if stack:
            answer[i] = stack[-1]
    
        stack.append(num)
    return answer